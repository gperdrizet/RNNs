# Sequence learning with RNNs

An introduction to Recurrent Neural Networks (RNNs) for sequence modeling tasks. This repository contains educational notebooks that progress from basic RNN concepts to a full sentiment analysis pipeline using TensorFlow/Keras.

## Notebooks

| Notebook | Description |
|----------|-------------|
| [alphabet_rnn.ipynb](notebooks/alphabet_rnn.ipynb) | **Start here.** A gentle introduction to RNNs using a simple next-character prediction task. Learn how RNNs maintain hidden state to process sequences. |
| [sentiment_analysis.ipynb](notebooks/sentiment_analysis.ipynb) | Full sentiment analysis pipeline on Twitter data. Covers tokenization, GloVe embeddings, Bidirectional GRU, and model evaluation with visualizations. |
| [sentiment_analysis_activity.ipynb](notebooks/sentiment_analysis_activity.ipynb) | **Activity:** Extend the baseline GRU model by adding convolutional layers to create a CNN-RNN hybrid architecture. Compare performance against the baseline. |

## Getting started

### Prerequisites

- [VS Code](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Setup

The demos are intended to run in a devcontainer development environment using VS code. The RNNs demo environment is derived from the [gperdrizet/deeplearning-devcontainer](https://github.com/gperdrizet/deeplearning-devcontainer) template repository and uses the `deeplearning-nvidia` base image from [gperdrizet/docker-images](https://github.com/gperdrizet/docker-images).

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RNNs
   ```

2. Open in VS Code:

3. When prompted, click **"Reopen in Container"** (or use the command palette: `Dev Containers: Reopen in Container`).

4. Wait for the container to build and install dependencies.

5. Open a notebook and run the cells.

### Tensorboard

To view the demo training runs in TensorBoard visit http://localhost:6006 while the devcontainer is running.

## Data

### Twitter

The sentiment analysis notebooks use the [SemEval-2017 Task 4 Twitter dataset](https://alt.qcri.org/semeval2017/task4/index.php?id=data-and-tools)<sup>1</sup>. The data was parsed and assembled into a single parquet file for easy loading using the script [`src/format_data.py`](https://github.com/gperdrizet/RNNs/blob/main/src/format_data.py).

### Tokenization

The demo notebooks use the Twitter specific [NLTK TweetTokenizer](https://www.nltk.org/api/nltk.tokenize.casual.html#nltk.tokenize.casual.TweetTokenizer).

### Embeddings

The [GloVe](https://nlp.stanford.edu/projects/glove)<sup>2</sup> Twitter embeddings (~1.5GB) will also be downloaded automatically on first run.

## References

1. Sara Rosenthal, Noura Farra, and Preslav Nakov. 2017. [SemEval-2017 Task 4: Sentiment Analysis in Twitter](https://alt.qcri.org/semeval2017/task4/index.php?id=data-and-tools). In *Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)*, pages 502–518, Vancouver, Canada. Association for Computational Linguistics.

2. Jeffrey Pennington, Richard Socher, and Christopher Manning. 2014. [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf). In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1532–1543, Doha, Qatar. Association for Computational Linguistics.