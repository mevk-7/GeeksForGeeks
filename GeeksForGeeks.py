#Author ---> Vikrant Karn
from selenium import webdriver
import pdfkit
import os


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.maximize_window()
    #pdfkit.from_url('http://stackoverflow.com','test.pdf')
    driver.get('http://www.cdn.geeksforgeeks.org/fundamentals-of-algorithms/')
    li=driver.find_elements_by_tag_name('ol')
    try:
        os.mkdir('GeeksforGeeks')
    except: pass
    os.chdir('./GeeksforGeeks')
    di=['Analysis of Algorithms','Searching and Sorting','Greedy Algorithms','Dynamic Programming','Pattern Searching','Other String Algorithms','Backtracking','Divide and Conquer','Geometric Algorithms','Mathematical Algorithms','Bit Algorithms','Graph Algorithms','Randomized Algorithms','Branch and Bound','Quizzes on Algorithms','Misc']
    co=0
    i=0
    sub=['Introduction DFS and BFS','Minimum Spanning Tree','Shortest Paths','Connectivity','Hard Problems','Maximum Flow']
    while i<(len(li)):
        print(i)
        try:
         os.mkdir(di[co])
        except:
            i+=1
            co+=1
            continue 
            #pass
        os.chdir('./'+di[co])
        print(di[co])
        
        
        if (di[co]=='Graph Algorithms'):
            for  it in range(6):
                x=li[i].find_elements_by_tag_name('a')
                try:
                    os.mkdir(sub[it])
                except: 
                    pass
                os.chdir('./'+sub[it])
                for j in x:
                    name=j.text
                    link=j.get_attribute('href')
                    try:
                        pdfkit.from_url(link,name+'.pdf')
                    except:
                        pass
                i+=1
                os.chdir('..')

        else:
            x=li[i].find_elements_by_tag_name('a')
            for j in x:
                name=j.text
                link=j.get_attribute('href')
                try:
                    pdfkit.from_url(link,name+'.pdf')
                except:
                    pass
        os.chdir('..')
        i+=1
        co+=1

