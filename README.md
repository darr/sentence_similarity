# SimilarityCompute
Sentence Similarity compute based on cilin, hownet, simhash, wordvector,vsm models，  
基于同义词词林，知网，指纹，字词向量，向量空间模型的句子相似度计算。  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

# results
```shell
sentence1:南昌是江西省的省会
sentence2:北京乃中国之首都
cilin 0.9
hownet 0.7857142857142857
simhash 0.46875
simtoken 0.4715704505415333
simvsm 0.0


sentence1:我是中国人，我深爱着我的祖国
sentence2:中国是我的母亲，我热爱她
cilin 0.8375
hownet 0.8068181818181819
simhash 0.734375
simtoken 0.8240455276180504
simvsm 0.7126966450997984


sentence1:一群高贵气质的差人在处罚违章动物
sentence2:城管执法，若不文明会导致很多不公平事故
cilin 0.6363636363636362
hownet 0.36916208791208793
simhash 0.53125
simtoken 0.20195795723403823
simvsm 0.0


sentence1:小明去了姥姥家，姥姥给他买了一本童话书
sentence2:我外婆早早的就出去了，给我带回来一本恐怖小说
cilin 0.7000000000000001
hownet 0.4841269841269841
simhash 0.53125
simtoken 0.5974486426178804
simvsm 0.16903085094570325
```

# 理论简介

中文句子相似度计算，目前包括word-level和sentence-level两个level的计算方法。  
前者的思想是通过对句子进行分词，分别计算两个比较句中所含词汇的相似度。  
后者主要采用句子建模的方法。 

# 1、word-level的方法

word-level的方法包括两个核心问题，  
1）word之间的相似度计算问题 ，  
2) 将句子中多个word相似度进行加权融合的问题。  

## 1）word之间相似度的计算问题  

word之间相似度的计算问题，分成两种，  
一种是形态（包括字符级的形态以及词语级的形态）上的相似，  
这个在英语中是比较可行的，英语中可以将词语进行词干化，  
而在中文中并不适用，  
例如‘爸爸’和‘父亲’实际上是同一个词，但是形态上的相似度是0，这显然是不行的。  

因此诞生了第二种方法，基于语义知识库的词语相似度计算。  
目前中文的语义知识库比较著名的有董振东先生研发的hownet以及哈工大研发的大词林，其中：  
hownet将每个词的意义分解为多个义原，  
例如：{爸爸：human|人,family|家,male|男}，{父亲：human|人,family|家,male|男}  

在cilin中，则对相似词语进行了编码，  
如 {Ah04A01= 父 父亲 爷 爹 大 翁 爸爸 老子 爹爹 老爹 阿爹 阿爸 椿 太公 大人 爸 生父 爹地 慈父}  

可以看出‘爸爸’和‘父亲’都属于同一个语义编码。  
因此，借助外部语义知识库，可以在一定程度上解决中文的形态问题。  
但受限于知识库的词汇有限，难以大规模的使用。  

## 2）基于word相似度的句子相似度加权问题        

这里涉及基于词相似的句子相似度度量，  
主要常用的jaccard编辑距离， 语义距离相似度。  
其中：给定两个句子s1,s2:  
words1 = [token for token in s1]  
words2 = [token for token in s2]  

### jaccard距离     

SIM(s1,s2) = intersection(words1, words2)/union(words1, words2)

### 语义距离    

SIM(s1, s2) = 1/2 * (sum(max(sim(word1,word2) for word1 in words1 for word2 in words2))/len(words1) + sum(max(sim(word2,word1) for word2 in words2 for word1 in words1))/len(words2)  

# 2、sentence-level的方法  

sentence-level包括两种方法，  
核心思想是使用向量空间模型，将句子进行向量表征。  
具体包括两种方式：  
1）基于word-vector的组合  
2）sentence-vector  

## 1）基于word-vector的组合  

目前常用的是使用预先训练好的word-embdding向量，  
对于一个句子，将词向量的每一位进行加和或求平均。  
另外一个是使用one-hot结合tfidf对句子进行vsm表示的方法。  

## 2）基于sentence-vector的方法    

目前关于sentence建模的方法包括skip-gram, cbow的doc2vector建模方法，  
基于autoencoder的建模方法，基于skip-thought的句子建模方法等。  
我们通常认为，基于sentence-vector的方法能够更好的保留句子的语义信息，能够在一定程度上弥补1）的词袋缺点。    

# 1、输入       

1）hownet.dat:知网的词语义原表示    
2）cilin.txt:同义词词林    
3）token2vector.bin：中文字符向量    
4）word2vector.bin：中文词语向量    

# 2、方法    

1）sim_cilin.py：基于同义词词林的相似度计算  
2）sim_hownet.py: 基于hownet的相似度计算  
3）sim_simhash.py: 基于指纹的相似度计算   
4）sim_tokenvector.py：基于字符向量的相似度计算  
5）sim_wordvector.py：基于词向量的相似度计算   
6）sim_vsm.py：基于向量空间模型one-hot的相似度计算    

# 总结

1、从以上的结果来看，simvsm的方法在短句中貌似不工作  
2、基于语义知识库的方法效果要好一些  
3、基于wordvector得到的方法与基于语义知识库的方法效果相当  
4、将这几种方法进行融合，应该会有更好的效果，内部的计算规则还有待优化   

