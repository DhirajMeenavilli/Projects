# Thoughts and Occurances

## With Respect to the Consequences of Fat Tails in Statistical Statements

It may be that the very infrastructure on which we model may be wrong, and that far too many normality and modelability assumptions are made, and this may present a crack that has yet to be discovered, and requires only such a tail event to occur for it to blow up on us. Though it is always possible that rather everything is fine.

If not however it may reveal to what more things are certain to be beyond our grasp at the moment, and could potentially focus efforts or just make use of data science, where such use is good.  

In addition, it may very well present oppurtunities for new investing practices, such as effectively short selling hype, the way value investors buy statistcally profitable bundles of cheap securities. Perhaps they may even reveal things about the others such as growth about value and value about growth, fragility about value and value about fragility. As well it may present oppurtunities to reconsider a host of other decisions entirely built on on flawed foundations.

It appears most RL and other neural network techniques also tend to be dependant on assumptions of normality and tending toward normality sufficient a large sample size.

If this is the case then perhaps an RL model can be devolped such that it can more quickly determine what kind of function, or tail coefficient a distribution should be generated with and thus behave accordingly.

Watching for large deviations within a collection of data i.e. outliers of some consistent but low frequency is likely the best way to find if the domain is fat tailed, and so dangerous for things like an RL model to learn/predict on. 

However the solution cannot be to just simply do nothing, even for us as people we have to learn to take appropriately hedged bets meaning thurough understandings of risk, which itself may be something that might be difficult to analyse from a statistical perspective i.e with use of past data, though it may not be. This may be one of the interesting ideas to investigate.

A point about Standard Deviation and beyond, for any 2 vectors assuming their L1/mean is the same if the dispersion is wider for one than another, say [1,1] and [2/3,4/3] the l2/STD is going to be larger, and the difference will increase explosively the larger an l norm you take. 

Hence Taleb advises using the MAD for both stability,and communicability of an idea of average deviation, though even still you can't make much of a prediction with MAD, it's just more useful to describe what it ddescribes. So I don't know how we would solve the quandry of what action/exposure to take for an RL prgram, except for that it must be a hedged one in potentially fat tailed situations. 

Infinite variance models based on thing like Cauchy Stable or 2 sided Pareto or Student T with a small tail exponenet can all simmulate fat tailed conditions, although they may all have different shapes, the tail exponent chosen for a Student T, does appear to be pretty robust, so it can occasionaly be useful to see grey swans assuming the data fit reasonably well. This means we can find a reasonable price for the insurance of a situation, as well as how to intelligently take exposure so we don't go bust, perhaps that idea can be trnaslated over to the world of RL or just ML in general.

Tools such as Mutual Information, as opposed to measures of correlation or Pearsons coefficient of determination as well as regime analysis and the previously explored power law fitting of data may help provide insight into how one can watch and add value in fat tailed or multi modal situations, by effectively offering to the operaator how to tailor exposure/show what the various regimes may look like.

If there's heuristics such as intermediate shapes of a distribution for a sum i.e. rates of convergance to figure out what kind of distribution a variable is being approximately drawn from assuming the soft conditions of independance and identical originating distribution. Then it could be the case that RL or just NN could also devolp better heuristics, or different heuristics and tell us which distributions we might be looking at. Taken with the distributions which we derrive it might be from the regular heuristics and rules Taleb reveals gives us potentially greater insight to what we can say it might not be, and what the worst case distribution we need to protect against. 

This could possibly be done by making the reward, the percentage likelihood that a stream of values observed came from a certain distribution with certain parameters and make the penalty the max confidence the machine had in a distribution being a candidate prior to it being disqualified (<0.1% confidence of it being a candidate). Possibly could use just the penalty but I think the rough idea makes sense.

Tests such as using the EVT heurstic of sigma(u) which supposes that the difference in probability of a maximum under an unknown distribution should as that maximum goes out further and further towards the finite or infinite right endpoint of the unknown distribution have it's conditional distribution beyond a given value be no different than if the distriution were some Generalised Pareto Distribution. (Though I'm not quite sure how this ties into the theorem about the GEVD, and the idea that the MDA for any power law distribution is the Frechet distribution).

Most of the time for a security or whatever is being analysed it is sufficient to realise what class a given variable likely belongs to, and then proceeding to explore that class for what distribution it may be, and what parameters it may have like tail exponent, location, scale, shape, etc.

Potentially as opposed to using sigmoid, or leaky ReLUs, a use of weighted calls, with different times to expiration to create curvuture may be useful, though it would certainly need to be tested. 

Additionaly by performing a "battery" of tests, we can find not only if a tail is Paretian in distribution but also potential assymetrys and dependences by noting changes one unit removed in time (before and after), and then comparing the number of maxs to a Harmonic Number of how many maxs would be the case given random shuffled data. 

If you have data generated from a right skewed distribution with infinite variance and a bounded left side then you will likely endup with partial sums in their pre asymptotic phase producing lower "mean" values than the true mean. This is the case as the mode is to the left of the mean resulting in a lower value such as discussions of Gini and percentiles. It also creates the illusion of things such as increasing inequality due simply to the fact that a better approximation is occuring due to a higeher n value bring the mean closer to the true value. However this can be somewhat fixed by using a tail exponenet approximation via the log-log linear regression and using the lowest tail exponent or generating a stochastic tail exponenet, which can both serve the purpose of allowing for extrapolation and generating a psuedo distribution which can tell you how far the mode is from the mean thus allowing for a band aid in the form of a semi corrected parametric estimate.

If you have a set of data which appears to be of an undefined mean i.e of alpha < 1 but you know there's a maximum like for example, a companys sale are topped out by GDP, or the loss in value of an asset is bounded by it's current full capitalisation, then you can use a method by which you take the tail as is, and then find some coditional mean in the tail beyond some threshold via some fancy math, and from that work out the properties of the original distribution that could help in deciding what could happen on average, with war for example Taleb calculates it as casualties are bounded by the human population, and beyond some threshold like 50,000 thousand casualties, the conditonal mean is about 30,000,000 which is roughly 3x as much as is the case with the simple arithementic mean, therefore from a strict statistical point of view the world is possibly more dangerous than we think and violence may not be on the decline we might just be in a good period.

Given that we try to estimate an amount of uncertainity about the average of a distribution via the standard deviation / variance, it would only make sense to estimate some level of uncertainity about that uncertainity, and keeping constant with that train of thought and assuming we have no level of uncertainity about which we are certain then we can go infinitely deep, leading to an explosion of the second moment which creates very thick tails. So unless there is a decreasing level of uncertainity as we go out, or some point at which we are sure that's the amount of uncertainity we explode out effectively to power laws. Or as Taleb puts it, "Fat Tails are the Product of Recusrsive Epistemic Uncertainty".

Also in the same way that OTM options are convex to Std. Dev. as in as the Standard Deviation rises by 1 unit the value of the OTM option rises quicker than 1 unit and that rate accelerates the more Std. Dev. increases. They are also convex to uncertainity about the Standard Deviation, this is because as uncertainity about it rises it could be higher and so prices of OTM options rise. And in the same fashion the expectation or mean of a power law distributed variable is convex to the tail exponent and the uncertainity about the tail exponent. This convexity to uncertainity for some reason though appears to make the true mean assymetrically higher than lower than the in sample mean, leading to a further downward biased estimate of the expectation, but why and to what degree I'm entirely uncertain.

Given that we take p-values to be generated of a power law meta distribution, the probability of atleast one p-value in a series of expiriments being less than 0.05 is almost 100% even if the truth of the matter is weak or even no evidence against the Null Hypothesis, just due to the stochastic nature of an expiriment. The fixes suggested are looking for p-value < 0.005 or my preffered solution is to report the full distribution of p-values expirienced as the expirirment was done over and over as opposed to just reporting the minimum/statistically significant point p-value, so that it can be understood and fitting a distribution to it we can find the median p-value and MAD etc. to get a better idea of what's going on. Obviously stochasticity of the tail exponent introduuces further complications, but perhaps not a bad first step.

CLT states that your partial sum as Sn = A large enough number, the distribution will come out to being Gaussian. The Law of Large Numbers then says as the CLT kicks in your mean will end up concentrating and concentrating until you get a Dirac stick for Sn = A very large number i.e. low to no variance as n gets vry big. The problem is for power laws it takes a very very large n for those 2 things to kick in, assuming there even is a mean or a finite variance.

There is possibly much to be gained even under fat tails, to making bets with the Kelly criterion, thereby avoiding any chance of risk, as the geometric mean is maximised and greater than 0, and also to the idea of the St. Petersburg resolution of buying insurance on risky instruments, to boost the geometric mean, at the cozt of the arithemetic one which was also emphasised by Spitznagel, and also the notion of volatility harvesting as a way to allow for the use of arithmetic average to be in your favor, given taxes and commisions can be minimised in such a way to allow it to be viable. This allows for better thinking on a portfolio level, under any regime, pbviously however correlation of risks still need to be considered and diversified to whatever extent they can be or countered via insurance, etc. It should be added however that a fractional Kelly bet is better as there are things such as uncertainties due to epistimic boundries, so even with a pretty suree thing, one should bet less than Kelly optimal, even after the kelly optimal has been reduced to be conservative, this allows for possibly over conservatism in some sense but also defenitley a lack of overbetting, and thus does not allow for the ruin. 

Additionally ideas of information such as entropy, and the notion of a private wire giving truer odds than is the case being priced on the tote board or in the market alllows for better thinking about the fundamental analysis of a situation, and how best to bet on any given situation, as well as allowing for a more disinterested more distant approach to equity selection.

I am now convinced of the idea that through thurough witiling down of possibilities is the best way to approach almost any problem. With a disconfirmatory cynical perspective, than with a onfirmatory positivisst perspective.

## With Repect to Work and Learning

It is not unreasonable to approach any obstacle of life or work as things to be tackled by a process of refined reasearch, with hypothesis, observations, analysis, and what that could possibly tell you about the domain with which you're interacting.

I find more and more that where things, fail, break, and don't break is substantially more important to understand then where they do. I suppose this is encapsulated in the 2 phrases, "It ain't what you know, it's what you know for sure but just aint so." and "I want to know where I'll die so I'll never go there". I think possibly just following those 2 ideas and constantly looking for where failure is likely and avoiding them leaves just the success to take care of itself.

With respect to incentives, if you can learn the incentives of others and choose to be incentivised by something else you can focus on the fundamentals while giving enough of the thing the other is incentivised by to gain what you desire as secondary goals etc. (For ex. Some look for the Githib commits, so a few a day, or even 1 a day is enough to give the recruiter the feeling they can sell me, etc. and I can at the sam time mark myself by how cool my projects are etc. but in doing enough of the first I can get a good job, cool interviews etc.)

It appears to learn anything in the real world you have to really really struggle, and deal with these very treacherous learning environments. Some of it comes easily in plain english, but there come cracks and nuances which are too large or difficult to capture with verbalistic notions. On the other hand, there are these deeply thought out, rich texts which require such a great degree of contextual knowledge and fundamental knowledge of assumptions that it not only overwhelms but can very easily trick you if you are not comfortable with trying to see where a theorem, idea, or model fails, especially so if you don't take care to appropriately hedge against error occuring.

Perhaps this doesn't need an explicit statement but I've noticed that the ability to learn an idea deeply rests both on giving oneself time to digest an idea, while attacking it from multiple angles but it also resides in the neccessary mandate of actively engaging with the idea everytime one engages with it.

As I get deeper into dedicating myself to actually studying and pursuing intrests, I find I am bound by 2 things. 

    1. Intrest in other things spikes up and I am unable to get to it, until I finish what currentlyholds my intrest. This is primarily because if I allow myself to get interested in a lot of things I'll start a lot of things and never finish a lot of things, which I would find more unsatisfying than simply having done fewer things.

    2. My focus can be very variable depending on the day, and I often find myself in this state where I want to learn yet my brain has no capacity for the focus I need to put up and the lack of stimulation from the thing. The latter is begining to wane somewhat as I become more and more comfortable with things like reading and watching lectures. Yet the first acts as a very hard obstacle although my genuine disintrest in more uninteresting things is acting to help me feel more comfortable. I find it's defenitley a tradeoff. But one which is proggressively more favorable.

I've found additionally, there's a sweet spot to be struck between understanding a concept in full depth and just accepting that it will make sense as the greater picture comes to be, and if it still bothers you once you've gone deep into the dexcursion you can always come back to it.

Also I found additionally, the smallest possible step is that which is repeatable every day.

In addition to approaching learning from this more relaxed, yet consistently struggling way and by focusing on taking time to digest and break down ideas in your head, it is not ideas that you learn, but rather tools that you can then use to cut a problem down, analyse the subproblems, solve the subproblems via a method of rigirous disconfirmation, understand their consequences, and put it back together in a comprehensible and usable way for yourself and others.

Deep unthinking relaxation is also profoundly important to not just learning, but to the congealing of oneself with their humanity.

It comes to be that almost all political situations boil down to goals, available paths/branching paths, incentives, and leveraging actions to generate the largest optionality, this comes as the natural other hand to single minded obsession. 

Problem solving effectively boils down to understanding the concepts, principles, and techniques you can apply to a situation, figuring out the structure of the system in which the problem is encased and exploiting said structure to have it be shaped more amenably. It also comes to how to come up with ideas when you run out, i.e. perturbing the structure, which comes with gathering more tools and where to look for solutions.

Failure to take things from theory to reality is likely a function of mismatches between the context of theory and the medium to which you are trying to translate that theory, i.e. rhymes to paper, books to excel forecasts, or algorithims to code.

Truly resting is a critical skill, yet one entirely ununderstood by myself, and likely everyone else who works more than they think.

It is certainly curious that rest requires a slowness and abatement which the ideal of consistency cannot permit. I wonder if those things thus become related as in those who can fall back and take a moment can then speed up and get ahead, akin to the ideas in the Art of War.

The balance in order to achieve competency and the volatility that is correlated with progress have to be finely balanced lest one become complacent or unstable.

I also seem to get very wrapped up in my own thoughts and context to the point where it becomes indiscernable from the have to's of my day like breathing and eating. However unlearning that, as well as how to commit tentatively such that I can reallign as my goals change will be a massive boon.

With respect to making things you just go layer by layer like a painter, and as you layer better and better you get closer and closer to making the beautiful art you wanted to make even if it's radically different from the intial vision. Also remember you go from:

A -------> A
↑          |
|          |
|          ↓
S -------> S

Where S stands for situation and A for abstraction

## With Repect to Teaching and Sharing

When you have people of all different cultureal contexts, domain knowledge, incentives, and levels of resistance to different proposed ideas, one has to fundamentally come at the practice of teaching and sharing as not correct or incorrect but rather perhaps a fundamental set of tenants and beliefs, and the exact scope of the conversation.

Empathy is also extremely important. As the state and beliefs of an individual will really make a difference to how the conversation should be had.

No matter how many successes you have, you will always have failures, and they will almost certainly loom larger than any win can make up for however, the key to it is to keep going keep moving, and keep trying. Because as long as you are not defeated, you are not defined by your losses.

Deep traumas or even misalligned feelings relating to things like work, and research etc. are one of the key hurdles to enjoying life to the fullest, because meaningful work is one of those things that you can not have for a long time, but once you get your life becomes much more satisfying and well paced.

You do become at some point the person someone looks to guidance be ready for the responsibility by making as many mistakes as possible without doing anything obviously dumb.

## With Repect to Greatness

Being considered great is a function of the historical process and the human memory. Both of which are outside the realm of your control, geniuses are forgotten and fools are immortalised. One can only foxus on maximising their chances at greatness by truly being great, which means one can only maximize their chances by doing the work and pushing oneself without breaking.

It is highly correlated with doing things unconventionally, or in a way that is public but remote, surprise I suppose is the largest correlative factor.

Greatness is not a product or contribution but rather who we are in every moment we are. What makes heroes and people great are those who never quit trying to be good, unencumbered by money or any incentive other than to be as good as possible. But all those ideals feel fake and 2 dimensional, to be real and great is something more profound and unknown then that. It is in accepting failure, showing up, being reliable, looking out for people when you can, and trying to spend the brief moments we have on this precious jewel expierencing life doing something mildly interesting and having fun. There is no purpose to greatness other than to serve as an other objective we can seek to optomize, but there is nothing to optimize only to expirience and you should just pick expiriences which lead to more and more desirable states, till you have one beyond which you do not need, and resist the want for more.

Not everyone starts gifted and privelleged from birth, we just start out where we do on our own broken path in life, and if we get lucky so we get a fighting chance, take risks well, and leverage the situations adaquetly to the extent we are able i.e. give it our best shot, then we may end up at a place we cannot even begin to imagine but can only hope that we are still kind and able to put love back into the world.

Fundamentally the whole idea behind incentives and the reasoning for any action can be broken down into a belief of how one can go about maximising time spent being free (taking any action and getting the result of the best action on a 100% deterministic basis) and being bound (each action has it's own value and thus some are prefferable to others under the constraints of the situation). The greater the split of ones to time to the former the freer they are the more it is dedicated to the latter the more dutiful and advanced one becomes. Ideally there would be sufficient of the latter such that one can spend a greater and greater portion of their time doing the former. Thus in effect maximising it, and this question then effectively drives all our actions, with our subconcious correlations filling in what it is we need to accquire/own/have in order to get to such a state.

One has to understand where if their current potential is maintained how great they can be, and one must be staisfied in both knowing where the boundary of that is, and wherein they can grow, and when it is sufficient for life enough to be like a dream. As well it helps in being able to recognise what kind and how great someone else is, it can allow for you to surround yourself with greats, younger, older, and of the same cohort as you and allows you to know when to listen to someone else and when not to. I t allows for the creation of the use of friends and resources while limiting or prohibiting the abuse of said friends and resources.

Science is much like all of expirience itself a very personal pursuit. Used to address the issues and difficulties, and make real the dreams of an individual, therefore in addition to doing it yourself, supporting those most marginalised to do their science their way is the best things we can do to promote the dream. To make as many scientists as possible, not just data crunchers but creatives and artistic types to become scientifically savvy.

I think the commonality which I find to be most intense among all the people I consider truly great is the dedication to the fundamentals to ignore all the noise and distraction of approval, and results. To focus single mindedly and obsessively on the fundamentals of the entity to which you are applying your process of deconstruction and solution to and the process of deconstruction and solution itself.

The second is having great people around themselves, which I suppose now in the internet age is a lot easier, and there's a lot more great people with which one can surround themselves.

The third is working on cool and great things, which also is easier to find, and more to do now in the age of instant communication, and centeralised knowledge stores.

## With respect to Science

All science effectively boils down to discovery and development, see a problem which intrests you for some personal reason, popularity, money, artistic expression, equalisation, etc. etc. and then discover abstractions which allow for an acceptable amount of lossiness in the abstracted state, then devolp techniques for that state which leverage the paarticularities of the abstraction and then recovert in as lossless a way as possible and then if desired refine and do it over and over again until satisfied.

Science in my opinion is not even neccessarily the understanding of why something works, it is simply the finding of repetable behaviour, if you can find behaviour which determinstically, probablistically, or randomly repeats in exactly the same way. That knowledge can then be documented, and digested to refine how it's leveraged.

Science is also the great bastardizer of our myths showing us what is and most often what isn't the case if we're just willing to see through repeated trial and expiriment but in doing so also shows us the true depth and richness of life.

People used to have math duels and math partially to one up each other and solve strange occurances of logical consequences and occassionally model with them. Weird world, weirder times without much incentive to keep secrets of mathematics.