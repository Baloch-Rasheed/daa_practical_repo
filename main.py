from sub_string_matching import sub_string_matching_algorithm

def main():
    txt = 'My name is Kamal Khan, and they call me Kamal'
    ptrn = 'Kamal Khan'

    result = sub_string_matching_algorithm(text=txt, sub=ptrn)

    print('results: ', result)


if __name__ == "__main__":
    main()



