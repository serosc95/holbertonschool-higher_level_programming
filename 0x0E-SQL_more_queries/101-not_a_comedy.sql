-- Import the database dump from hbtn_0d_tvshows

SELECT title FROM tv_shows
WHERE title NOT IN (
	SELECT title
        FROM tv_shows
	INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
	INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
        WHERE tv_genres.name = "Comedy")
ORDER BY title
