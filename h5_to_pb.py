from keras import backend as K
from keras.models import load_model
import tensorflow as tf
import argparse
import os
from model import ElementwiseMaxPool, RepeatElements



def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    """
    Freezes the state of a session into a pruned computation graph.

    Creates a new computation graph where variable nodes are replaced by
    constants taking their current value in the session. The new graph will be
    pruned so subgraphs that are not necessary to compute the requested
    outputs are removed.
    @param session The TensorFlow session to be frozen.
    @param keep_var_names A list of variable names that should not be frozen,
                          or None to freeze all the variables in the graph.
    @param output_names Names of the relevant graph outputs.
    @param clear_devices Remove the device directives from the graph for better portability.
    @return The frozen graph definition.
    """

    from tensorflow.python.framework.graph_util import convert_variables_to_constants
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        # output_names = output_names or []
        # output_names += [v.op.name for v in tf.global_variables()]
        # Graph -> GraphDef ProtoBuf
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = convert_variables_to_constants(session, input_graph_def,
                                                      output_names, freeze_var_names)
        return frozen_graph


parser = argparse.ArgumentParser(description='Convert Keras .h5 to Tensorflow .pb')
parser.add_argument('input_file_h5', help='path to input the .h5 file')
parser.add_argument('output_file_pb', help='path to output the .pb file ')

args = parser.parse_args()

K.set_learning_phase(0)

model = load_model(args.input_file_h5,
                   custom_objects={'ElementwiseMaxPool': ElementwiseMaxPool,
                                   'RepeatElements': RepeatElements})

output_names = [out.op.name for out in model.outputs]
for name in output_names:
    print(name)

frozen_graph = freeze_session(K.get_session(), output_names=output_names)

print(model.summary())

folder, filename = os.path.split(args.output_file_pb)
tf.train.write_graph(frozen_graph, folder, filename, as_text=False)

print('Convert Done!')
