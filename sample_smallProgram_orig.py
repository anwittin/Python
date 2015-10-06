# Our epic programmer dict from before
epic_programmer_dict = {'tim berners-lee' : ['tbl@gmail.com', 111],
                         'guido van rossum' : ['gvb@gmail.com', 222],
                         'linus torvalds' : ['lt@gmail.com', 333],
                         'larry page' : ['lp@gmail.com', 444],
                         'sergey brin' : ['sb@gmail.com', 555],}


print epic_programmer_dict

personsName = raw_input('Please enter a name: ').lower()


# Looks up the name in the dictionary

try:
# Tries the following lines of texts and if
        
# there are no errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print personsInfo

except:
# If there are errors, then this code gets run

        print 'No information found for that name'
