# paper notes  

 * 2 TPU pods - split batch 1/2 on each pod, computed in parallel.  
 * Fat bandwidth between the two pods.  
 * Jump in processing when going to very large parameters. Does size of LM problem fit very large structure?  
 * Transformer architecture, decoder-only for application. Language Model already trained with encoder.  
 * Very large tokens (540 billion), multiple languages, math, code 5% (Github Public with open License).  
 * Generator - translation, sequence of logical phrases.  

 * Pathways is a 2019 paper, how to efficiently parallelize very large training.  
