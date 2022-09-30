
'''Αριθμός Μητρώου: Π21230'''


def stats(lst, strng):
    max = len(strng)
    output = []
    for elements in lst:
        if elements != '':
            times = strng.count(elements)
            result = str(int(times/max * 100)) + "%"

            '''Για να κάνουμε print το ποσοστό εμφάνισης κάθε γράμματος της λίστας στο strng:'''
            '''print('Letter:', elements, " has a", result, "apperance in", strng)'''
            output.append(result)
    '''Το παρακάτω return κάνει return τα ποσοστά με τη σειρά που έχουν δοθεί στην αρχική λίστα'''
    return output


'''Η κλήση της συνάρτησης stats(lst, strng) γίνεται:'''
'''stats(['a', 'e', 'p', 'v', 'i', 'x'], "'Hello. This is a project for the University.'")'''
