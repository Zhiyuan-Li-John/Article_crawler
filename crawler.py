from module import arxiv_reader

if __name__ == "__main__":
    # please add your interest topic word below
    interest_topic = ["", "", "", "", "", ""]

    # load arxiv class
    arxiv = arxiv_reader()

    # load topic words 
    arxiv.get_your_interest(interest_topic)

    # go through all the newest articles
    arxiv.read_articles()

    # search the relevant article and record it in the record folder
    arxiv.find_match()

    #print out match result
    # arxiv.print_out_matching()
