# (Revision) Choice with replacement

This exercise is a revision of something we have done before.  We are going to present the problem a different way, however.

We want to model taking a ball out of an urn.  This urn contains `N` balls in total `R` of which are green and the remaining `(N-R)` of which are red.  We will generate a random variable, X, based on the colour of the ball that is selected.  If the ball is green this random variable will equal 1.  If it is blue the random variable will equal 0.  Your task in this exercise is to complete the function `choice` that generates this random variable using this rule.  This function takes `N` and `R` in input.  The meanings of these variables are described above.  The function should return the value of the random variable that is defined in the manner that was explained above. 

When your function is complete a graph with the values of these random variables will be generated.  
