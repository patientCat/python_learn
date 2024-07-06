# svm

## 01 svm 进行2分类


## 02 svm 如何进行多分类

对于多分类问题有2种处理方法

第一种

one-to-one 即每次只对2个类别进行分类，忽略其他数据集，可见需要C(n,2)个分类器，C(n,2)=n(n-1)/2

![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202406282231435.png)

第二种

one-to-rest 即每次将数据集看做是目标和目标其他数据集合进行分类，需要n个分类器。

每次只需要将目标和其他数据集进行分类即可。

![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202406282233074.png)