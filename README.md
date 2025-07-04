# meilisearch_mcp
专为Trovelocal项目打造的mcp服务器。

目前提供meilisearch查询，通过meilisearch为大模型提供私人知识库的专有知识，提升大模型解决专业领域问题的能力。

## 使用

- 修改utils.py中的meilisearch服务器地址和api_key（MEILI_URL、MEILI_API_KEY）。

- 运行meili_mcp.py

![image-20250704124123638](README.assets/image-20250704124123638.png)

- 添加mcp服务器到客户端工具。下面以vscode+cline为例。

![image-20250704124247045](README.assets/image-20250704124247045.png)



![image-20250704124315713](README.assets/image-20250704124315713.png)



![image-20250704124605609](README.assets/image-20250704124605609.png)



![image-20250704124627754](README.assets/image-20250704124627754.png)

添加成功后，把模式切换为Act：

![image-20250704124922536](README.assets/image-20250704124922536.png)

开始提问。

### 问1：刑法第二十条

![image-20250704124953178](README.assets/image-20250704124953178.png)

回答：

![image-20250704125159599](README.assets/image-20250704125159599.png)

继续追问： 从mcp查询：有没有具体案例？

![image-20250704125305705](README.assets/image-20250704125305705.png)

回答的都是知识库中存储的知识：

![image-20250704125536139](README.assets/image-20250704125536139.png)

### 问2：fortigate版本识别有什么办法

![image-20250704125919030](README.assets/image-20250704125919030.png)

回答：

![image-20250704130000829](README.assets/image-20250704130000829.png)

![image-20250704130013655](README.assets/image-20250704130013655.png)
