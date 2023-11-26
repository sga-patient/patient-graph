from keplergl import KeplerGl

def makeMap():
    map = KeplerGl(height=600, width=600)
    return map

def main():
    makeMap()

if __name__ == "__main__":
    main()