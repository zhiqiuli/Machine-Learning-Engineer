/*
shelf_similarity
shelf_j    shelf_i    similarity
3725194    4301024    13.00
3725194    1275382    5.00
3725194    2912513    11.22
3725194    3814118    10.91
3725194    4325524    10.70
3725194    7985280    10.51
3725194    3735822    10.45
3725194    9862357    7.00
3725194    8477888    4.00
3725194    4876693    3.00
3725194    3659116    2.00
3725194    4704533    11.31



shelf_info
shelf_id    shelf_name                      top_cp_name
4301024    Sharpie Ultra Fine Point Markers    home
9157964    Paint Pens & Markers                Arts
3278193    Permanent Markers                   Arts
4704533    Metallic Sharpies                   home
2912513    Drawing Markers                     home
3814118    White Sharpies                      home
4325524    Markers in Bulk                     Arts
7985280    Crayola Thin Tip Markers            Arts
3735822    Watercolor Markers                  home
9862357    Art & Drawing Markers               home
4051643    Sharpie                             Arts
8477888    Paint Markers                       Arts
1275382    Elmer's Art Supplies                home
4876693    Shop Markers by Brand               home
1629377    Crayola Specialty Markers           home
3659116    Sharpie Fine Point Markers          Arts
3725194    Color Markers                       Arts

    
Question 1 For each shelf,generate the 8 most similar shelves.no duplicated rank. keep the shelf if it is not in  shelf_info table. Organize the output by shelf_j and rank.

sample  answer
shelf_j    shelf_i    similarity    rank    shelf_topcp_j    shelf_topcp_i    shelf_name_j                          shelf_name_i
3725194    4301024    13.00             1    Arts               home            Sharpie Ultra Fine Point Markers    Color Markers
3725194    9157964    13.00             2    Arts               Arts            Paint Pens & Markers                Color Markers
3725194    3278193    11.37             3    Arts               Arts            Permanent Markers                   Color Markers
3725194    4704533    11.31             4    Arts               home            Metallic Sharpies                   Color Markers
3725194    2912513    11.22             5    Arts               home            Drawing Markers                     Color Markers
3725194    3814118    10.91             6    Arts               home            White Sharpies                      Color Markers
3725194    4325524    10.70             7    Arts               Arts            Markers in Bulk                     Color Markers
3725194    7985280    10.51             8    Arts               Arts            Crayola Thin Tip Markers            Color Markers
*/

-- answer to 1st question

with tmp1 as (
	select shelf_j,shelf_i,similarity
	from shelf_similarity),
    
tmp2 as (
	select t.shelf_j,t.shelf_i,t.similarity,s.top_cp_name as shelf_topcp_j,s.shelf_name as shelf_name_j
	from tmp1 t
	left join shelf_info s
	on t.shelf_j = s.shelf_id
	)

select shelf_j,
	   shelf_i,
	   similarity,
	   rank() over (partition by shelf_j order by similarity desc, shelf_i) as 'rank',
	   shelf_topcp_j,
	   shelf_name_j
from tmp2
order by shelf_j desc, 'rank'

--

with tmp1 as (
    select ss.shelf_j, ss.shelf_i, ss.similarity, si.shelf_name as shelf_name_j, si.shelf_topcp as shelf_topcp_j
    from shelf_similarity ss
    left join shelf_info si
    on ss.shelf_j = si.shelf_id
),

tmp2 as (
    select ss.shelf_j, ss.shelf_i, ss.similarity, shelf_name_j, shelf_topcp_j, si.shelf_name as shelf_name_i, si.shelf_topcp as shelf_topcp_i
    from tmp2 ss
    left join shelf_info si
    on ss.shelf_i = si.shelf_id),

tmp3 as (
    select shelf_j, shelf_i, similarity,
    rank() parition over(shelf_j order by similarity desc, shelf_i) as 'rank',
    shelf_topcp_j, shelf_topcp_i, shelf_name_j, shelf_name_i
    from tmp2)

select *
from tmp3
where 'rank' <= 8
order by shelf_j, rank, shelf_i

--

https://www.db-fiddle.com/

 /* CREATE TABLE */
CREATE TABLE shelf_similarity(
shelf_j INT(11),
shelf_i INT(11),
similarity DECIMAL( 10 , 2 )
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,4301024,13.00
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,1275382,5.00
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,2912513,11.22
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,3814118,10.91
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,4325524,10.70
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,7985280,10.51
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,3735822,10.45
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,9862357,7.00
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,8477888,4.00
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,4876693,3.00
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,3659116,2.00
);

/* INSERT QUERY */
INSERT INTO shelf_similarity( shelf_j,shelf_i,similarity )
VALUES
(
    3725194,4704533,11.31
);


 /* CREATE TABLE */
CREATE TABLE shelf_info(
shelf_id INT(11),
shelf_name VARCHAR( 100 ),
top_cp_name VARCHAR( 100 )
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    4301024,'Sharpie Ultra Fine Point Markers','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    9157964,'Paint Pens & Markers','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    3278193,'Permanent Markers','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    4704533,'Metallic Sharpies','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    2912513,'Drawing Markers','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    3814118,'White Sharpies','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    4325524,'Markers in Bulk','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    7985280,'Crayola Thin Tip Markers','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    3735822,'Watercolor Markers','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    9862357,'Art & Drawing Markers','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    4051643,'Sharpie','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    8477888,'Paint Markers','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    1275382,'Elmers Art Supplies','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    4876693,'Shop Markers by Brand','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    1629377,'Crayola Specialty Markers','home'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    3659116,'Sharpie Fine Point Markers','Arts'
);

/* INSERT QUERY */
INSERT INTO shelf_info( shelf_id,shelf_name,top_cp_name )
VALUES
(
    3725194,'Color Markers','Arts'
);





