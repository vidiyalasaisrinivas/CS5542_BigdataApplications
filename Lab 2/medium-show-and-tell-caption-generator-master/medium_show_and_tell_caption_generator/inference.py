#greg

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from nltk.translate.bleu_score import sentence_bleu

import logging
import math
import os

import tensorflow as tf

from medium_show_and_tell_caption_generator.caption_generator import CaptionGenerator
from medium_show_and_tell_caption_generator.model import ShowAndTellModel
from medium_show_and_tell_caption_generator.vocabulary import Vocabulary

list_of_images = os.listdir("C:\\Users\\vidiy\Desktop\BDA\class\medium-show-and-tell-caption-generator-master\imgs")
img_files_paths = r""
for image in list_of_images:
    img_files_paths += "C:\\Users\\vidiy\Desktop\BDA\class\medium-show-and-tell-caption-generator-master\imgs\\"+image+","


img_files_paths = img_files_paths[:-1]
# print(img_files_paths)
FLAGS = tf.flags.FLAGS


tf.flags.DEFINE_string("model_path", r"C:\Users\vidiy\Desktop\BDA\class\medium-show-and-tell-caption-generator-master\model\show-and-tell.pb", "Model graph def path")

tf.flags.DEFINE_string("vocab_file", r"C:\Users\vidiy\Desktop\BDA\class\medium-show-and-tell-caption-generator-master\etc\word_counts.txt", "Text file containing the vocabulary.")

tf.flags.DEFINE_string("input_files", img_files_paths,
                       "File pattern or comma-separated list of file patterns "
                       "of image files.")

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def main(_):
    model = ShowAndTellModel(FLAGS.model_path)
    vocab = Vocabulary(FLAGS.vocab_file)
    filenames = _load_filenames()

    generator = CaptionGenerator(model, vocab)
    output = ""
    for filename in filenames:
        with tf.gfile.GFile(filename, "rb") as f:
            image = f.read()
        captions = generator.beam_search(image)
        print("Captions for image %s:" % os.path.basename(filename))
        for i, caption in enumerate(captions):
            # Ignore begin and end tokens <S> and </S>.
            sentence = [vocab.id_to_token(w) for w in caption.sentence[1:-1]]
            sentence = " ".join(sentence)
            output += "imgID: "+os.path.basename(filename)+", Caption: "+sentence+"\n"
            print("  %d) %s (p=%f)" % (i, sentence, math.exp(caption.logprob)))
    o = open("output1.txt","w+")
    o.write(output)

# Change to read a folder name of captions
def _load_filenames():
    filenames = []
    for file_pattern in FLAGS.input_files.split(","):
        filenames.extend(tf.gfile.Glob(file_pattern))
    logger.info("Running caption generation on %d files matching %s",
                len(filenames), FLAGS.input_files)
    return filenames



if __name__ == "__main__":
    tf.app.run()

