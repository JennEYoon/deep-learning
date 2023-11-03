# From Scratch Neural Networks, Transformers    

### Andrej Karpathy:  
<img src="./Andrej_Karpathy.jpg" width=150>   

 * YouTube Channel: https://www.youtube.com/@AndrejKarpathy    
   - My motivation for creating this channel: https://twitter.com/karpathy/status/1577746577463967745    
 * Github notebooks:   
   - https://github.com/karpathy/makemore  
   - https://github.com/karpathy/nanoGPT  
 * Website -- https://karpathy.ai/   

>Notes from YouTube video:
Intro: ChatGPT, Transformers, nanoGPT, Shakespeare
Let's build GPT: from scratch, in code, spelled out.

Andrej Karpathy
242K subscribers
3,222,233 views  Jan 17, 2023

We build a Generatively Pretrained Transformer (GPT), following the paper "Attention is All You Need" and OpenAI's GPT-2 / GPT-3. We talk about connections to ChatGPT, which has taken the world by storm. We watch GitHub Copilot, itself a GPT, help us write a GPT (meta :D!) . I recommend people watch the earlier makemore videos to get comfortable with the autoregressive language modeling framework and basics of tensors and PyTorch nn, which we take for granted in this video.

Links:
- Google colab for the video: https://colab.research.google.com/dri...
- GitHub repo for the video: https://github.com/karpathy/ng-video-...
- Playlist of the whole Zero to Hero series so far:   

 • The spelled-out intro to neural netwo...  
- nanoGPT repo: https://github.com/karpathy/nanoGPT
- my website: https://karpathy.ai
- my twitter:  

Supplementary links:
- Attention is All You Need paper: https://arxiv.org/abs/1706.03762
- OpenAI GPT-3 paper: https://arxiv.org/abs/2005.14165 
- OpenAI ChatGPT blog post: https://openai.com/blog/chatgpt/
- The GPU I'm training the model on is from Lambda GPU Cloud, I think the best and easiest way to spin up an on-demand GPU instance in the cloud that you can ssh to: https://lambdalabs.com . If you prefer to work in notebooks, I think the easiest path today is Google Colab.

Suggested exercises:
- EX1: The n-dimensional tensor mastery challenge: Combine the `Head` and `MultiHeadAttention` into one class that processes all the heads in parallel, treating the heads as another batch dimension (answer is in nanoGPT).
- EX2: Train the GPT on your own dataset of choice! What other data could be fun to blabber on about? (A fun advanced suggestion if you like: train a GPT to do addition of two numbers, i.e. a+b=c. You may find it helpful to predict the digits of c in reverse order, as the typical addition algorithm (that you're hoping it learns) would proceed right to left too. You may want to modify the data loader to simply serve random problems and skip the generation of train.bin, val.bin. You may want to mask out the loss at the input positions of a+b that just specify the problem using y=-1 in the targets (see CrossEntropyLoss ignore_index). Does your Transformer learn to add? Once you have this, swole doge project: build a calculator clone in GPT, for all of +-*/. Not an easy problem. You may need Chain of Thought traces.)
- EX3: Find a dataset that is very large, so large that you can't see a gap between train and val loss. Pretrain the transformer on this data, then initialize with that model and finetune it on tiny shakespeare with a smaller number of steps and lower learning rate. Can you obtain a lower validation loss by the use of pretraining?
- EX4: Read some transformer papers and implement one additional feature or change that people seem to use. Does it improve the performance of your GPT?
