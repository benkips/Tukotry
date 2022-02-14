def run(self, args, opts):
    # Get the list of Crawlers
    spd_loader_list = self.crawler_process.spider_loader.list()
    # Traverse the crawls
    for spname in spd_loader_list or args:
        self.crawler_process.crawl(spname, **opts.spargs)
        print("The crawl that starts at this time:" + spname)
    self.crawler_process.start()