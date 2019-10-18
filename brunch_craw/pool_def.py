#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def pool_def(category_list,writer_list):
    res_dict = {}
    tmp_set=[]
    tmp=[]
    for i,name in enumerate(category_list):
        print("%d"%i)
        res_dict[name] = tmp
        for text_url in writer_list[i]:
            tmp.append(tmp_set)
            tmp_set = []
            html = requests.get('https://brunch.co.kr/@{text_url}'.format(text_url=text_url))
            soup = BeautifulSoup(html.text, 'html.parser')
            ss = soup.find_all('p')
            tmp_set = []
            for j in ss:
                tmp_set.append(j.text)
    return res_dict

