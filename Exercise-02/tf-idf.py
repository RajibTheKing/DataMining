
import math

class tf_idf:
    def __init__(self):
        self.docs = dict()
        self.docs[1] = "fast car highway road car"
        self.docs[2] = "car car bike fast fast"
        self.docs[3] = "road road highway fast wheel"
        self.docs[4] = "bike wheel car wheel"

        self.N = len(self.docs) # Total Number of Documents
        print(self.N)
        self.vocabulary = []
    
    def buildVocabulary(self):
        print("Vocabulary\n#############")
        for x in self.docs:
            words = self.docs[x].split()
            for y in words:
                if y not in self.vocabulary:
                    self.vocabulary.append(y)
        
        for x in self.vocabulary:
            print(x)

    def calculateTF(self):
        print("\nTF\n######################")
        termFrequency = dict()

        for x in self.vocabulary:
            freq = []
            for y in self.docs:
                words = self.docs[y].split()
                numberOfWords = len(words)
                cnt = 0
                for w in words:
                    if w == x:
                        cnt = cnt + 1
                freq.append(cnt / numberOfWords)
            termFrequency[x] = freq

        for x in self.vocabulary:
            print(x + " => ", end = '')
            for y in termFrequency[x]:
                print(str(y) + " ", end = '')
            print("")

        return termFrequency



    def calculateIDF(self):
        print("\nIDF\n######################")
        docFrequency = dict()
        for x in self.vocabulary:
            cnt = 0
            for y in self.docs:
                if x in self.docs[y]:
                    cnt = cnt + 1

            docFrequency[x] = cnt

        docIDF = dict()
        for x in self.vocabulary:
            docIDF[x] = math.log10(self.N / docFrequency[x])
            print(x+ ": " + str(docIDF[x]))
        
        return docIDF

    def calculateTFIDF(self, tf, idf):
        print("\nTF-IDF\n######################")
        for x in self.vocabulary:
            for i in range(len(tf[x])):
                tf[x][i] = tf[x][i] * idf[x]
        
        for x in self.vocabulary:
            print("%10s => " % x, end="")
            for y in tf[x]:
                print("%10.5f " % y, end = '')
            print("")

                



def main():
    calc = tf_idf()
    calc.buildVocabulary()
    tf  = calc.calculateTF()
    idf = calc.calculateIDF()
    tfidf= calc.calculateTFIDF(tf, idf)



if __name__ == '__main__':
    main()
