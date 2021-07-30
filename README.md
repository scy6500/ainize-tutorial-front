If you want to use the **API** of this project, please check the link below  

**New Pride and Prejudice with GPT-2 API** : https://ainize.ai/scy6500/ainize-tutorial-server

---
# New Pride and Prejudice with GPT-2
When reading a novel, have you ever wished you could change its plot? What if you could use an AI to do so? For this experiment, we chose the novel "Pride and Prejudice."  

![](https://i.imgur.com/8VxLe38.png)

#### But, what If

- They fell in love at first sight?
- Mrs. Elizabeth didn't believe Mr. Wickham when he slandered Mr. Darcy?
- Mr. Darcy didn't send a letter containing the truth to convince her?
- Mr. Wickham and Mrs. Lydia (Elizabeth’s younger sister) didn't run away at night?
- etc…

What if the outcome of each incident had been different? Would they still be in love? With these curiosities in mind, we will train an AI model(GPT-2) with pride and prejudice and re-write a novel using it.

### How to Use?
1. Using Ainize Demo

Enter text into an input box and click the Submit button to get results. By dragging a **slider at the sidebar**, users can set the length of tokens for the result. DEMO is available in this [link](https://main-ainize-tutorial-front-scy6500.endpoint.ainize.ai/).

![](https://i.imgur.com/3OMerJT.png)

2. Using Ainize API

Use POST method as endpoint and send base_text and length as parameters
```
curl -X POST "https://main-ainize-tutorial-server-scy6500.endpoint.ainize.ai/predict" \
-H "accept: application/json" -H "Content-Type: multipart/form-data" \
-F "base_text="I love him. He's not proud. I was wrong. I was entirely wrong about him."" -F "length=150"
```
Information about the API can be found in this [link](https://ainize.ai/scy6500/ainize-tutorial-server?branch=main).

### How to Make?
Check out [this tutorial](https://comcom.notion.site/Tutorial-for-Ainizer-s-Project-10a1531521ea40a684120d1093b338f1).  In this tutorial, we will show how to fine-tune and deploy the GPT-2 model on Ainize as a live, easy-to-use service.

![](https://i.imgur.com/rRvKasw.png)