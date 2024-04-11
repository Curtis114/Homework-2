# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution  
path: tokenB->tokenA->tokenD->tokenC->tokenB  
Swap tokenB to tokenA: amountIn = 5, amountOut = 5.655321988655322  
Swap tokenA to tokenD: amountIn = 5.655321988655322, amountOut = 2.458781317097934  
Swap tokenD to tokenC: amountIn = 2.458781317097934, amountOut = 5.088927293301516  
Swap tokenC to tokenB: amountIn = 5.088927293301516, amountOut = 20.129888944077447  
Final balance in tokenB: 20.129888944077447  

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

