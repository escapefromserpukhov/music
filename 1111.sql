insert into executor (executor_name)
values ('Noize MC'), ('КиШ'), ('Green day'), ('LP'), ('Nirvanna'), ('Дора'), ('Гречка'), ('Timberlake');

insert into janr (janr_name)
values ('Рэп'), ('Рок'), ('Альтернатива'), ('Гранж'), ('ПОП')

insert into album (album_name,year_of_release)
values ('Орфей и Эвридика', 2018), ('Камнем по голове', 2012 ), ('Mirrors', 2005 ), ('Боже, храни кьют-рок', 2021), ('Не за что', 2021),
('insomniac', 2013), ('Meteora', 2003), ('Nevermind', 1991)


insert into  track (track_name, dlitelnost, album_id)
values ('Голос и струны',120,1), ('Дурак и молния',180,2),('Apologize',120,3),
('Дора дура',150,4),('Люби меня люби',60,5),('Killer',180,6),('Мантра',140,1),('Втюрилась',140,4),
('Suit & Tie',160,3),('Come as You Are',240,8),('Smells Like Teen Spirit',260,8),('Lithium',180,8),
('Numb',170,7),('Foreword',200,7),('«Рыбак»',120,2)

INSERT INTO collection_of_songs(collection_name, year_of_release) 
	values('Сборник1', 1970), ('Сборник2', 2014),
		('Сборник3', 2018), ('Сборник4', 2019),
		('Сборник5', 2019), ('Сборник6', 2020),
		('Сборник7', 2020), ('Сборник8', 2020)
		
insert into janr_executor (janr_id, executor_id)
values  (1,1), (1,2),
		(2,3), (2,4),
		(3,8), (4,7),
		(5,5), (5,6)
		
insert into executor_album (executor_id, album_id)
values(1,1), (2,2), (3,3), (4,4),
		(5,5), (6,6), (7,7), (8,8)
		
insert into track_collection (track_id, collection_of_songs_id)
values (1,1), (3,1), (2,2), (4,2), (9,3), (11,3), (10,4), (12,4), 
		(13,5), (15,5), (14,6), (5,7), (7,7), (6,8), (8,8)
		
insert into janr_executor (janr_id, executor_id)	
VALUES(3,7), (4,3)
