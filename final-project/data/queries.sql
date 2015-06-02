#planned queries: number of characters in request, number of upvotes relative to downvotes,
#whether post was edited, total number of upvotes, number of posts on RAOP on request,
#account age at request
CREATE TABLE 'pizzas' (
  'CHARACTERS' int(20) DEFAULT NULL
  'UPVOTES' int(20) DEFAULT NULL
  'EDITED' DEFAULT NULL
  'TOTAL UPVOTES' DEFAULT NULL
  'NUMBER OF POSTS' DEFAULT NULL
  'ACCOUNT AGE' DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;