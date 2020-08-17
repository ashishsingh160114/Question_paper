print("---------First Micro Assignment for Python Development---------")
questions={ "Q.No.1. Which of the following is not a result of cell division?":{"correct":"c", "answers":['Growth','Repair','Metabolism','Reproduction']},
            "Q.No.2. Mark the incorrect pair":{"correct":"c", "answers":['Hydra – Budding','Flatworm – Regeneration','Amoeba – Fragmentation','Yeast – Budding']},
            "Q.No.3. Which of the following is incorrect for reproduction ?":{"correct":"b", "answers":['Unicellular organisms reproduce by cell division','Reproduction is a characteristic of all living organisms','In unicellular organisms, reproduction and growth are linked together','Non-living objects are incapable of reproducing']},
            "Q.No.4. Mark the incorrect statement w.r.t. metabolism ":{"correct":"d", "answers":['Microbes exhibit the metabolism','It is the property of all living forms','The metabolic reactions can be demonstrated in-vitro','It is not a defining feature of life forms']},
            "Q.No.5. Non-living objects exhibit/show ":{"correct":"d", "answers":['Property of self-replication','Evolution','Self-regulating interactive systems','Reversible growth']},
            "Q.No.6. Which statement is false about the growth shown by non-living objects? ":{"correct":"d", "answers":['The growth occurs from outside','The growth is reversible','The growth is due to the accumulation of material on the surface','The growth is intrinsic']},
            "Q.No.7. Local names of various plants and animals ":{"correct":"d", "answers":['Help in recognizing organisms worldwide','Are used universally','Are specific and distinct names','Vary from place to place']},
            "Q.No.8. Which of the following is incorrect w.r.t. Binomial nomenclature? ":{"correct":"d", "answers":['Biological names are generally in Latin','The first word in a biological name represents the genus','Biological names are printed in italics','The first word of the genus starts with a small letter']},
            '''Q.No.9. What do A, B and C represent in the given scientific name respectively? Mangifera-(C) indica-(B) Linn(A) ''':{"correct":"c", "answers":['Generic name, specific name and author’s name','Specific name, generic name and author’s name','Author’s name, specific name and generic name','Generic name, author’s name and specific name']},
            "Q.No.10. Which of the following is incorrect regarding scientific names? ":{"correct":"a", "answers":['These are also known as common names','These ensure that each organism has only one name','These have two components – the generic name and specific epithet','These are universally accepted names']},
            "Q.No.11. According to binomial nomenclature, every living organism has ":{"correct":"b", "answers":['Two scientific names with single component','One scientific name with two components','Two names, one Latin and other common','One common name with three components']},
            "Q.No.12. Which of the following is incorrect w.r.t. Species? ":{"correct":"b", "answers":['A group of individual organisms with fundamental similarities','Two different species breed together to produce fertile offsprings','Human beings belong to the species sapiens','Panthera has many specific epithet as tigris, leo and pardus']},
            "Q.No.13. Taxonomy deals with ":{"correct":"d", "answers":['Development of zoological parks','Study of kinds and diversity of microorganisms only','Evolutionary relationships between organisms','Classification of diverse organisms in different taxa']},
            "Q.No.14. Which of the following features are not shown by scientific names of various organism? ":{"correct":"c", "answers":['They consists of two components','They have Latin origin','They always have “linn” abbreviation at the end of second component','They are printed in italics']},
            "Q.No.15. The correct sequence of taxonomic study of a newly discovered organism is ":{"correct":"d", "answers":['First classification then identification, nomenclature and characterization','First identification then classifying organism and then characterizations and nomenclature','First nomenclature then characterization, identification and classification','First characterisation then identification and classification and then nomenclature']},
            "Q.No.16. Which one of the following statements given below is not included in universal rules of nomenclature? ":{"correct":"b", "answers":['Generic names and specific epithet should be in Latin words','Generic name is immediately followed by name of taxonomists who described it firstly','Generic name must begin with capital letter','All letters of the specific name must be small']},
            "Q.No.17. Find the correct sequence of taxonomic categories. ":{"correct":"b", "answers":['Division -> Kingdom -> Genus -> Order','Species -> Genus -> Family -> Order','Class -> Order -> Family -> Division','Kingdom -> Class -> Species -> Order']},
            "Q.No.18. Which of the following is a class? ":{"correct":"a", "answers":['Mammalia','Sapindales','Primate','Poales']}, "Q.No.19. ______ is the assemblage of families which exhibit a few similar characters ":{"correct":"d", "answers":['Class','Genus','Species','Order']},
            '''Q.No.20. Fill in the blanks A and B. Kingdom -> Phylum -> [A] -> Order ->[B] ''':{"correct":"c", "answers":['A - Genus; B - Species','A - Family; B - Class','A - Class; B - Family','A - Species; B - Division']},
            '''Q.No.21. Match the following columns Column-I Column-II a. Binomial nomenclature (i) Carolus Linnaeus b. Generic name (ii) Muscidae c. Family (iii) Panthera d. Systema naturae ''':{"correct":"b", "answers":[' a(i), b(iii), c(iii), d(ii)','a(i), b(iii), c(ii), d(i)','a(ii), b(i), c(i), d(iii)','a(iii), b(i), c(ii), d(i)']},
            "Q.No.22. Genus is a category which comes in between the ":{"correct":"a", "answers":[' Family and Species','Class and Family','Order and Phylum','Kingdom and Class']},
            "Q.No.23. Three different genera Solanum, Petunia and Datura are placed in the family ":{"correct":"d", "answers":['Poaceae','Anacardiaceae','Hominidae','Solanaceae']},
            "Q.No.24. Cat and dog are placed in which families respectively ":{"correct":"d", "answers":['Felidae and Hominidae','Muscidae and Felidae','Poaceae and Canidae','Felidae and Canidae']},
            "Q.No.25. Which one of the following criteria is/are essential and form the basis of classical taxonomic studies? ":{"correct":"d", "answers":[' Ecological information of organisms','Development process','External and internal structure','External structure']},
            '''Q.No.26. In which of the following pair of category, greater is the difficulty of determining the relationship to other taxa at the same level, thus the problem of classification becomes more complex? ''':{"correct":"c", "answers":[' Genus and species','Tribe and genus','Division and phylum','Species and family']},
            '''Q.No.27. In taxonomic hierarchy, which of the following group of taxa will have less number of similarities as compared to other? ''':{"correct":"b", "answers":['Solanaceae, Convolvulaceae and Poaceae','Polymoniales, Poales and Sapindales','Solanum, Petunia and Atropa','Leopard, tiger and lion']},
            "Q.No.28. Taxonomic categories which come lower to the rank of class are ":{"correct":"b", "answers":['Order, phylum, family, species','Order, family, genus, species','Division, family, order, genus','Order, division, genus, species']},
            '''Q.No.29. Two animals A and B have similar morphological features and are fundamentally similar with each other, they must be treated as ''':{"correct":"a", "answers":['One biological species','Two distinct species','One biological genera','Two distinct genera']},
            "Q.No.30. A place used for storing, preservation and exhibition of both plants and animals is known as ":{"correct":"c", "answers":['Herbaria','Botanical Garden','Museum','Zoos']},
            "Q.No.31. Herbarium consists of ":{"correct":"d", "answers":['Collection of living plants','Collection of plant and animal specimens preserved in the containers','Preserved insects in boxes after collecting killing and pinning','Herbarium sheets carrying dried, pressed and preserved plant specimens on them']},
            "Q.No.32. National Botanical Research Institute consists of ":{"correct":"d", "answers":['Dried and preserved plant specimens only','Collection of preserved plant and animal specimens','Flora, manuals and monographs only','Collection of living plants for reference']},
            "Q.No.33. Key is ":{"correct":"c", "answers":['(1) A form of herbaria','A type of educational institute','A taxonomical aid used for identifying various organisms','Taxonomic category']},
            "Q.No.34. In zoological parks, animals are ":{"correct":"c", "answers":['Kept and preserved in containers or jars','Preserved in boxes after killing','Kept in protected environments under human care','Stuffed and then preserved']},
            "Q.No.35. For identifying organisms through key usually ":{"correct":"a", "answers":['Two contrasting characters are used','One similar character is studied','Two or more similar characters are used','Only one statement called lead is used']}, }
options=['a','b','c','d']
correct=0
total=len(questions)
answersheet={}
for i,j in questions.items():
    answersheet.update({i:j["correct"]})
input("\nThis is your Test Paper! \nPress ENTER to start!\n")
for p, q in questions.items():
    print(p)
    x=0
    for ans in q["answers"]:
        print(options[x] + ": " + str(ans))
        x +=1
    answer=input("\nType a, b, c, or d to select your answer. Then press ENTER.\n")
    if(answer==q["correct"]):
        correct +=1
    print("\n")
score=str((correct / total) * 100) + "%"
print("Quiz has Completed!\nYour score is " + score + " on this quiz.")
print("total no of Questions : ",total)
print("total correct answers : ",correct)

input("\nThank you..... your test has submitted!\nPress ENTER for Answersheet!\n")

for r,s in answersheet.items():
    print(r+''' The correct answer is :''' + s)
print("\n")
