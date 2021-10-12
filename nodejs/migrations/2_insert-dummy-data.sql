INSERT INTO users (name,email,password,phone,profile,bio)
VALUES ('Similoluwa Okunowo','rexsimiloluwa@gmail.com','some-silly-password','07085140175','{ "github":"https://github.com/rexsimiloluwah", "location":"Lagos, Nigeria", "twitter":"https://twitter.com/__ademola__", "linkedin":"linkedin.com/in/similoluwa-okunowo"} ', 'Crazy Guy'),
        ('Sopefoluwa Okunowo','sope.ayoade@gmail.com','some-silly-password','08062701345','{ "location":"Ile-ife, Nigeria", "twitter":"https://twitter.com/sopeseven", "linkedin":"linkedin.com/in/sope-okunowo"} ', 'Cool Guy | Finance');

INSERT INTO projects (title,description,link,category,tags,likes,userId, createdAt)
VALUES ('scrapix-cli','Node.js + TypeScript based image scraping CLI','https://github.com/scrapix-cli', 'CLI', ARRAY['Node.js','TypeScript','ImageScraping'],0,1, '2021-10-10 04:05:06');
