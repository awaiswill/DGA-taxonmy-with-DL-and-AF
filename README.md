## DGA-taxonmy-with-DL-and-AF
This work is associated with work on Domain Generating Algorithm (DGA) malware detection. DGA detection is based on deep learning hybrid model of CNN, LSTM and Attention models. This hybrid model classifies legitimate DNS samples from DGA generated malicious DNS samples. DGA sample are taken from a publically available repo from Bamabanek while legitmate benign DNS sample are taken from ALEXA top one million domain names. 
Since inception of deep learning models of LSTM and CNN, shallow nwteorks models like random forest classifier, hidden markove models and n-gram models are outperformed by these deep learning models.
First ever Deep Learning model is applied in 2016 on LSTM networks which successfully outperformed all shallow ML models in performance.
In 2017 First CNN based DGA detection is introduced and it also outperformed shallow ML models with good margin.
Then in 2018 hybrid approches of LSTM, BiLSTM and CNN networks are implemented with improved performance to single unit models. Later approaches augumented the attention model to these hybrid approaches for further improvement. These are named as ensembled models.

The Ensembled model achieved an optimal performance and we started to study all hyperparameters to optimize these implemented models. LSTM networks has property of retaining sequential information and CNN networks has property of retianing spatial information of input vectors. Addition of Attention model to LSTM networks further enhances its processing of sequential information.

This ensemble model approach has shown optimum performance and motivated our research work to focus on one model at a time for optimization. We focused on LSTM networks to be improved with its hyperparameters. In hypermeters we further narrowed to activation functions. Activation Functions are broadly categorised into fixed shape Non linear and rectifier shape activation functions. 
We focus on LSTM networks and in LSTM network we focus on fixed shape activation functions. Popular fixed shape Non linear AFs include sifmoid AF, Hyper tangent (TanH) and Swish AFs.  
