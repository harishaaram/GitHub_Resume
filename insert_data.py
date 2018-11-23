from app import db, ClickLink, OriginalLink

def InsertWebsites(links, table):
    try:
        for link in links:
            row = table(web_link = link)
            db.session.add(row)
            db.session.commit()
    except:
        pass

def InsertResumeLinks(resume_links, table):
    for id, position_title, res_link in resume_links:
        row = table(link_id = id, category_name = position_title, resume_link = res_link)
        db.session.add(row)
        db.session.commit()

if __name__ == "__main__":
    links = ['https://harishaaram.github.io/', 'https://www.meetup.com/PyDataChi/events/251222062/',
             'https://medium.com/@hramachandran/impact-of-linguistic-choice-of-words-in-news-articles-105122d099a5']

    resume_db = [(1, 'DA', 'www.da/harishaaram.github.io/'),(2, 'DA', 'www.da/pydata.speaker.com/'),
                 (1, 'DS', 'www.ds/harishaaram.github.io/'),(2, 'DS', 'www.ds/pydata.speaker.com/')]
    # InsertWebsites(links, OriginalLink)
    InsertResumeLinks(resume_db, ClickLink)


