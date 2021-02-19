# d'oh!
This is a simple, fun project to scale a pizza dough recipe and to play with Python and GitHub.

The recipe is based on [Gozney's _Simple Pizza Dough_](https://us.gozney.com/blogs/recipes/simple-pizza-dough) and is a basic dough of approximately 61% [hydration](https://thepizzaheaven.com/pizza-dough-hydration/). I have found it quite suitable for my amateur pizza-baking needs. It comes together quickly and is pretty easy to work with. I usually make the dough the day/evening before the day I want to cook, which gives the balls a nice long, slow rise in the refrigerator. Just take the balls out about 2 hours before you want to make pizzas.

With the original recipe, I found that dividing it into 3 balls worked best for me, yielding nice 12-13" pizzas. But I wanted to be able to scale it to yield any number of dough balls, so I divided the original by 1/3 as my base. The Python script simply multiplies the base amounts by the number you supply (it's not very sophisticated). It should work well for a range of about 2-10 balls. For more than 10 you will likely need to make some adjustments, not to mention invest in a commercial mixer. Less than 2, I'm not sure you really like pizza!?

### Tips
 - Use a good digital kitchen scale to weigh your ingredients.
 - Use "Tipo 00" flour, do not sub All-Purpose or bread flour. It really makes a difference.
 - Make pizza frequently to stay in practice!

### Usage
The script is intended to be run from a CLI with Python 3. Just supply the number of dough balls you'd like, for example:
```bash
python3 dough-doh.py 3
```
This will result in the following output:
```
INGREDIENTS FOR 3 DOUGH BALLS
-----------------------------
Water            305.0 g  
Dry Yeast          0.6 g  
Olive Oil         10.0 ml 
00 Flour         500.0 g  
Sea Salt          12.0 g  
```

You can supply the `-f` or `--fresh-yeast` flag if you are using fresh yeast instead of dry:
```bash
python3 dough-doh.py 2 -f
```
The proper amount of fresh yeast will go into the ingredients list (and dry yeast will be omitted):
```
INGREDIENTS FOR 2 DOUGH BALLS
-----------------------------
Water            203.3 g  
Fresh Yeast        1.0 g  
Olive Oil          6.7 ml 
00 Flour         333.3 g  
Sea Salt           8.0 g  
```

That's about it. _Mangia!_
