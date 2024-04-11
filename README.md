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
What is slippage in AMM:  
Constant Product Formula: Uniswap V2, like many AMMs, uses a constant product market maker model, which is represented by the formula x*y=k, where:  
x is the quantity of one token in the liquidity pool,  
y is the quantity of the other token, and  
k is a constant value.  
Price Determined by Pool's State: The price in such a model is determined by the ratio of x to y. When a trade occurs, it changes the quantities of x and y, thus changing the price.  
Slippage Occurs: The larger the trade in relation to the pool size, the more significant the impact on the ratio of x to y, leading to a noticeable difference between the expected and actual prices – this is slippage.  
How does Uniswap V2 address this issue:  
Price Impact Warning: Uniswap interface provides warnings for trades that are likely to have a high price impact, which is a form of slippage.  
Setting Slippage Tolerance: Users can set a slippage tolerance level to mitigate the risk of high slippage. If the price changes beyond this tolerance during the transaction execution, the transaction will revert.  
Routing Through Multiple Pairs: Uniswap V2 can route trades through multiple pairs to minimize slippage, especially for larger trades or less liquid pairs.  
Example:  
Let’s illustrate with an example. Suppose we have a token pair A and B in a Uniswap V2 pool:  
Pool before trade: 10,000 A and 5,000 B (k=50,000,000).  
You want to swap 1,000 A for B.  
Using the constant product formula:  
New quantity of A in pool = 11,000  
Calculate new quantity of B: 11,000*y=50,000,000 ⇒ y≈4545.45  
So, the amount of B received ≈ 5,000 - 4545.45 = 454.55 B  
However, if you expected a 1:2 ratio (i.e., 1,000 A for 500 B), the actual amount received (454.55 B) is less than expected. This difference is due to slippage.  

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
In Uniswap V2's UniswapV2Pair contract, 1,000 units of liquidity are subtracted during the initial liquidity minting to:  
Prevent Price Manipulation: It discourages initial liquidity providers from manipulating the price and then quickly removing their liquidity for a profit.  
Avoid Division by Zero: It ensures that the pool never has zero liquidity, which is important for preventing division by zero errors in the constant product formula used by Uniswap V2.  

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
In the UniswapV2Pair contract, when depositing tokens (not for the first time), the minting function uses a specific formula to determine liquidity token allocation. This is intended to:  
Maintain Proportionality: The amount of liquidity tokens minted is proportional to the depositor's share in the liquidity pool, ensuring fair distribution.  
Preserve Constant Product: The formula helps maintain the constant product formula x×y=k, crucial for the AMM mechanism in Uniswap.  
Prevent Dilution and Manipulation: It ensures that adding liquidity doesn't unfairly dilute the share of existing liquidity providers or allow for manipulation of the system.  
This approach upholds fairness in the allocation of liquidity tokens and ensures that rewards are proportionate to each provider's contribution.  

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
A sandwich attack is a type of trading manipulation that occurs in decentralized finance (DeFi) platforms, particularly in AMM-based decentralized exchanges like Uniswap. It impacts users initiating token swaps and works as follows:  
Detection of a Victim's Transaction: An attacker monitors the blockchain for large pending swap transactions from users.  
Front-Running: The attacker places their own swap transaction with a higher gas fee, buying the same asset the user is trying to buy, but before the user's transaction gets processed.  
Back-Running: After the user's transaction is executed, which typically drives the price up due to the initial purchase, the attacker immediately sells the asset they just bought, often at a higher price.  
This results in:  
The victim receiving less of the output token than expected due to the increased price caused by the attacker's front-running transaction.  
A potential loss to the victim as they buy high and sell low in a very short time frame.  
Sandwich attacks are a risk in decentralized environments because of the transparent and deterministic nature of blockchain transactions, which allows attackers to spot and exploit such opportunities.  

