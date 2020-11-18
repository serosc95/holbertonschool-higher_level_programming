-- Import the database dump from hbtn_0d_tvshows

SELECT name FROM tv_genres
WHERE name NOT IN (
	SELECT name FROM tv_genres 
	INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
        INNER JOIN tv_genres ON tv_show_genres.show_id = tv_shows.id
        WHERE tv_shows.title = "Dexter")
ORDER BY name
