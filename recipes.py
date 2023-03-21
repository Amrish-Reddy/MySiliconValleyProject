# Define all the ingredients
rice = "2 cups basmati rice"
chicken = "1 kg chicken"
spices = "1 tsp cumin, 1 tsp coriander, 1 tsp turmeric, 1 tsp chili powder"
onion = "2 sliced onions"
tomato = "3 chopped tomatoes"
ghee = "2 tbsp ghee"
yogurt = "1/2 cup yogurt"
ginger_garlic_paste = "2 tsp ginger garlic paste"
cream = "1/2 cup cream"
saffron = "1/4 tsp saffron"
cashews = "1/4 cup cashews"
raisins = "1/4 cup raisins"
sugar = "1 cup sugar"
water = "2 cups water"
milk_powder = "1/4 cup milk powder"
flour = "1 cup flour"
baking_powder = "1 tsp baking powder"
salt = "1/4 tsp salt"
oil = "For deep frying"
chickpeas = "1 cup boiled chickpeas"
potatoes = "2 boiled and mashed potatoes"
chaat_masala = "1 tsp chaat masala"
tamarind_chutney = "1/4 cup tamarind chutney"
puris = "10-12 puris"
pistachios = "1/4 cup chopped pistachios"
cardamom = "1/2 tsp cardamom powder"
lentils = "1 cup urad dal"
coconut = "1/2 cup shredded coconut"
curry_leaves = "10-12 curry leaves"
mustard_seeds = "1 tsp mustard seeds"

# Define all the instructions
def mix_ingredients(*args):
    print("Mix the following ingredients: ", end="")
    for ingredient in args:
        print(ingredient, end=", ")
    print()

chicken_biryani = [
    "Step 1: Wash and soak the rice in water for 30 minutes.",
    "Step 2: Heat ghee in a pan and fry the sliced onions until golden brown.",
    "Step 3: Add the chicken and spices and cook for a few minutes.",
    mix_ingredients(chicken, spices),
    "Step 4: Add chopped tomatoes and cook until the mixture is soft.",
    mix_ingredients(tomato),
    "Step 5: Layer the rice and chicken mixture in a large pot.",
    "Step 6: Add saffron, cashews, and raisins.",
    mix_ingredients(saffron, cashews, raisins),
    "Step 7: Add 4 cups of water and cook on low heat until the rice is cooked."
]

gulab_jamun = [
    "Step 1: Mix together milk powder, flour, and baking powder.",
    mix_ingredients(milk_powder, flour, baking_powder),
    "Step 2: Add yogurt and knead the dough until it is smooth.",
    mix_ingredients(yogurt),
    "Step 3: Shape the dough into small balls.",
    "Step 4: Heat oil in a pan and deep-fry the balls until golden brown.",
    "Step 5: Make a sugar syrup by boiling together sugar and water.",
    mix_ingredients(sugar, water),
    "Step 6: Add the fried balls to the sugar syrup and let them soak for 1-2 hours."
]

veg_manchurian = [
    "Step 1: Mix together grated vegetables, flour, and salt.",
    mix_ingredients("1 cup cornstarch, salt"),
"Step 2: Shape the mixture into small balls and deep fry in oil until golden brown.",
"Step 3: Heat oil in a pan and fry chopped garlic and ginger.",
mix_ingredients("2 cloves garlic, chopped", "1 inch ginger, chopped"),
"Step 4: Add chopped onions and fry until they are soft.",
mix_ingredients("1 onion, chopped"),
"Step 5: Add chopped bell peppers and cook for a few minutes.",
mix_ingredients("1/2 cup chopped bell peppers"),
"Step 6: Add soy sauce, vinegar, and tomato ketchup.",
mix_ingredients("2 tbsp soy sauce", "1 tbsp vinegar", "2 tbsp tomato ketchup"),
"Step 7: Add the fried vegetable balls and cook for a few minutes.",
"Step 8: Serve hot."
]

paneer_butter_masala = [
"Step 1: Heat ghee in a pan and fry chopped onions until golden brown.",
mix_ingredients(onion),
"Step 2: Add ginger garlic paste and fry for a few minutes.",
mix_ingredients(ginger_garlic_paste),
"Step 3: Add chopped tomatoes and cook until the mixture is soft.",
mix_ingredients(tomato),
"Step 4: Add spices and cook for a few minutes.",
mix_ingredients(spices),
"Step 5: Add cubed paneer and cook for a few minutes.",
mix_ingredients("200 gm paneer"),
"Step 6: Add cream and cook for a few minutes.",
mix_ingredients(cream),
"Step 7: Serve hot with naan or rice."
]

blackforest_pastry = [
"Step 1: Bake two chocolate cakes and let them cool.",
"Step 2: Make whipped cream by beating together cream, sugar, and vanilla essence.",
mix_ingredients("2 cups cream", "1 cup sugar", "1 tsp vanilla essence"),
"Step 3: Slice cherries and grate chocolate for decoration.",
mix_ingredients("1 cup sliced cherries", "1/2 cup grated chocolate"),
"Step 4: Place one cake on a plate and spread whipped cream over it.",
"Step 5: Add a layer of cherries and grated chocolate.",
"Step 6: Place the second cake on top and cover it with whipped cream.",
"Step 7: Decorate with cherries and grated chocolate."
]

pani_puri_chaat_masala = [
"Step 1: Make a tamarind chutney by boiling together tamarind, dates, jaggery, and spices.",
mix_ingredients("1/2 cup tamarind", "1/2 cup dates", "1/2 cup jaggery", "1 tsp cumin", "1 tsp coriander", "1 tsp red chili powder", "1 tsp chaat masala"),
"Step 2: Make a spicy water by mixing together mint leaves, coriander leaves, green chilies, chaat masala, and salt.",
mix_ingredients("1/2 cup mint leaves", "1/2 cup coriander leaves", "2 green chilies", "1 tsp chaat masala", "1/2 tsp salt"),
"Step 3: Crush puris slightly and fill them with boiled chickpeas and mashed potatoes.",
mix_ingredients("10-12 puris", "1 cup boiled chickpeas", "2 boiled and mashed potatoes"),
"Step 4: Dip the filled puris in the spicy water and serve with the tamarind chutney."]

Samosa = [
"Step 1: Make the dough by mixing flour, salt, and ajwain with water.",
mix_ingredients("2 cups flour", "1/2 tsp salt", "1/2 tsp ajwain", "water"),
"Step 2: Heat oil in a pan and fry chopped onions until golden brown.",
mix_ingredients(onion),
"Step 3: Add boiled and mashed potatoes and spices.",
mix_ingredients("2 boiled and mashed potatoes",spices),
"Step 4: Add chopped coriander leaves and mix well.",
mix_ingredients("1/4 cup chopped coriander leaves"),
"Step 5: Make small balls of the dough and roll them into circles.",
"Step 6: Cut the circles into halves and form a cone by sticking the edges together with water.",
"Step 7: Fill the cone with the potato mixture and seal the top with water.",
"Step 8: Deep fry the samosas until they are golden brown and crispy.",
"Step 9: Serve hot with tamarind chutney."]

idly_and_dosa = [
"Step 1: Soak rice and urad dal separately for 4-6 hours.",
mix_ingredients("2 cups rice", "1 cup urad dal"),
"Step 2: Grind the urad dal into a fine paste.",
"Step 3: Grind the rice into a slightly coarse paste.",
"Step 4: Mix the two pastes together and let the batter ferment overnight.",
"Step 5: Add salt to the batter and mix well.",
mix_ingredients("1 tsp salt"),
"Step 6: To make idlis, pour the batter into idli molds and steam for 10-15 minutes.",
"Step 7: To make dosas, heat a non-stick pan and pour a ladleful of batter on it.",
"Step 8: Spread the batter in a circular motion and cook until the dosa is crispy.",
"Step 9: Serve hot with sambar and chutney."]

butter_naan = [
"Step 1: Make the dough by mixing flour, yeast, sugar, salt, and yogurt with warm water.",
mix_ingredients("2 cups flour", "1 tsp yeast", "1 tsp sugar", "1/2 tsp salt", "2 tbsp yogurt", "warm water"),
"Step 2: Knead the dough well and let it rise for 1-2 hours.",
"Step 3: Divide the dough into small balls and roll them into naans.",
"Step 4: Heat a tawa or griddle and place the naan on it.",
"Step 5: Cook the naan on both sides until it is golden brown and puffy.",
"Step 6: Brush the naan with melted butter and serve hot with curry or dal."]

kulfi = [
"Step 1: Boil milk in a heavy-bottomed pan and let it simmer until it reduces to half.",
"Step 2: Add sugar and cardamom powder and stir well.",
mix_ingredients("1/2 cup sugar", "1/2 tsp cardamom powder"),
"Step 3: Let the mixture cool and add condensed milk.",
mix_ingredients("1 can condensed milk"),
"Step 4: Pour the mixture into kulfi molds or small glasses and freeze for 4-6 hours.",
"Step 5: Insert ice cream sticks into the kulfi and freeze for 6-8 hours or until firm.",
"Step 6: To remove the kulfi from the molds, run them under hot water for a few seconds and gently pull them out.",
"Step 7: Serve the kulfi garnished with chopped nuts and saffron."]

recipes = {
1: {"name": "Chicken Biryani", "instructions": chicken_biryani},
2: {"name": "Gulab Jamun", "instructions": gulab_jamun},
3: {"name": "Veg Manchurian", "instructions": veg_manchurian},
4: {"name": "Paneer Butter Masala", "instructions": paneer_butter_masala},
5: {"name": "Blackforest Pastry", "instructions": blackforest_pastry},
6: {"name": "Pani Puri Chaat Masala", "instructions": pani_puri_chaat_masala},
7: {"name": "Samosa", "instructions": Samosa},
8: {"name": "Idly and Dosa", "instructions": idly_and_dosa},
9: {"name": "Butter Naan", "instructions": butter_naan},
10: {"name": "Kulfi", "instructions": kulfi},
}

print("Welcome to the recipe maker!")
print("Here are the available recipes:")
for i in range(1, 11):
    print(f"{i} - {recipes[i]['name']}")

choice = int(input("Enter the number of the recipe you want to see: "))

print(f"\n{recipes[choice]['name']}:")
for step in recipes[choice]['instructions']:
    print(step)



