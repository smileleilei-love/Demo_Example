<h3>所谓的爬虫，其实就是--> 获取数据-解析提取数据-存储数据 </h3>

>就是通过编程向服务器发出网络请求，然后再对HTML解析，然后获取数据。需要了解并且学习计算机网络知识，`http`、`https` 、`网络协议`、`网络结构`(html语法标签、css、js)
python编程中的`数据结构`、`数据类型`、`逻辑结构`、`字典`、`字符串`、`列表`、`切片`、`条件语句`、`循环语句`等都是要弄清楚的。

《获取数据》我们绝大多数爬取的是网页 和 app。用到的请求库有 `request`、`urllib`、`aiohttp`、`selenium`。   <br>

pip install request -> request 主要方法<br>response = request.get(url)：获取网页网址信息 <br> response.encoding = 'UTF-8' 设置文本编码 <br>
response.status_code 请求响应码 <br> requests.request() 构造一个请求 <br> request.psot() 获取信息post 请求的信息<br> request.head() 获取请求头信息<br>
request.put() 获取put形式的<br>

![image](https://github.com/user-attachments/assets/f0c51e59-4ec4-4be6-b112-1f32060d8c5b)
