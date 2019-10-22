#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 게시글 크롤링

# import requests

# data = []
# json_data = {}

def def_craw(writer_list):
    global json_data
    global data
    tmp_text = []
    tag_keyword=[]
    
    tag_title,tag_nickname,tag_publish_date,tag_url,tag_url_plink = None,None,None,None,None
    tag_share,tag_like = str,str
    for i,url in enumerate(writer_list[0]):
        print("전체%d개의 게시글 중 %d번째 글 진행중" %(len(writer_list[0]),i+1))
        if tmp_text == []:
            pass
        else :
            json_data['title'] = tag_title.text  
            json_data['nickname'] = tag_nickname
            json_data['publish_date'] = tag_publish_date
            json_data['keyword'] = tmp_keyword   
            json_data['like'] = tag_like # like 없는 경우 ''
            json_data['share'] = tag_share # share 없는 경우 None
            json_data['comment'] = tag_comment # comment 없는 경우 ''
            json_data['url'] = tag_url
            json_data['url_plink'] = tag_url_plink 
            json_data['text'] = tmp_text

        data.append(json_data)
#         print(data)
        
        json_data = {} # 초기화
        tmp_text = [] # 초기화
        tmp_keyword = [] # 초기화
        
        # beautifulsoup 
        html = requests.get('https://brunch.co.kr/@@{text_url}'.format(text_url=url))
        soup = BeautifulSoup(html.text, 'html.parser')
        tag_text = soup.find_all('p') # 해당페이지의 본문
        tag_title = soup.find('title') # 해당페이지의 Title
        tag_nickname = soup.find("meta",{'name':'article:media_name'})['content'] # 글쓴이 닉네임
        tag_url = soup.find("meta",property='og:url')['content'] # 본주소
        tag_url_plink = soup.find("meta",property='dg:plink')['content'] # 암호주소? # 모바일?
        tag_publish_date = soup.find("meta",property='article:published_time')['content'] # 본주소
        tag_keyword = soup.find_all('a',href=re.compile('/keyword')) # 해당 글의 키워드
        tag_like = soup.find('span',{'class':'f_l text_like_count text_default text_with_img_ico ico_likeit_like #like'})
        tag_share = soup.find('span',{'class':'f_l text_share_count text_default text_with_img_ico'}) # 공유 수
        tag_comment = soup.find('span',{'class':'f_l text_comment_count text_default text_with_img_ico'}) # 댓글 수


        if tag_like == None:
            tag_like = "0"
        else:
            tag_like = tag_like.text # 좋아요 수
            
        if tag_share == None:
            tag_share == "0"
        else:
            tag_share = tag_share.text # 공유 수
        
        if tag_comment == None:
            tag_comment =="0"
        else:
            tag_comment = tag_comment.text
        
        for text in tag_text:
            tmp_text.append(text.text) # p태그 text
        for keyword in tag_keyword:
            tmp_keyword.append(keyword.text)

