import csv
from collections import defaultdict
from datetime import datetime

class Document:
    def __init__(self, title, file_size, category, created_on, updated_on, permissions):
        self.title = title
        self.file_size = int(file_size)
        self.category = category

        self.created_on = datetime.strptime(created_on, '%d.%m.%Y')
        self.updated_on = datetime.strptime(updated_on, '%d.%m.%Y')
        self.permissions = permissions

def load_documents(file_path):
    document_list = []
    with open(file_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for entry in reader:
            if len(entry) == 6:
                doc = Document(*entry)
                document_list.append(doc)
    return document_list

def tally_files_by_category(documents):
    tally = defaultdict(int)
    for doc in documents:
        tally[doc.category] += 1
    return tally

def top_largest_files(documents, limit=10):
    sorted_docs = sorted(documents, key=lambda x: (x.file_size, x.title), reverse=True)
    return sorted_docs[:limit]

def limited_access_presentations_2012(documents):
    restricted_docs = [
        doc for doc in documents 
        if doc.category == 'презентация' and doc.permissions == 'ограниченный' and doc.updated_on.year == 2012
    ]
    return sorted(restricted_docs, key=lambda x: x.title)

def large_videos_from_2011(documents):
    large_videos = [
        doc for doc in documents 
        if doc.category == 'видео' and doc.file_size > 100 * 1024 and doc.created_on.year == 2011 and doc.created_on.month > 6
    ]
    return sorted(large_videos, key=lambda x: x.file_size, reverse=True)

def run():
    documents = load_documents('files.csv')

    category_counts = tally_files_by_category(documents)
    print("Количество файлов по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    largest_files = top_largest_files(documents)
    print("\n10 самых больших документов:")
    for doc in largest_files:
        print(f"{doc.title}: {doc.file_size} Кбайт")

    limited_access_presentations = limited_access_presentations_2012(documents)
    print("\nПрезентации с ограниченным доступом, обновленные в 2012 году:")
    for doc in limited_access_presentations:
        print(doc.title)

    large_videos = large_videos_from_2011(documents)
    print("\nВидео размером больше 100 Мбайт, созданные во второй половине 2011 года:")
    for doc in large_videos:
        print(f"{doc.title}: {doc.file_size} Кбайт")

if __name__ == "__main__":
    run()
