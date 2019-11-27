-- lists all genres from hbtn_0d_tvshows displas the number of shows linked

SELECT t.name AS genre, COUNT(g.genre_id) AS number_of_shows FROM tv_genres t INNER JOIN tv_show_genres g ON t.id = g.genre_id INNER JOIN tv_shows s ON g.show_id = s.id GROUP BY genre ORDER BY number_of_shows DESC;
