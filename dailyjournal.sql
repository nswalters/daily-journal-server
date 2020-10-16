-- SELECT * from entries;
-- SELECT * from moods;

-- CREATE TABLE `entries` (
--     `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `concept` TEXT NOT NULL,
--     `entry` TEXT NOT NULL,
--     `date`  INTEGER NOT NULL,
--     `moodId` INTEGER NOT NULL,
--     FOREIGN KEY(`moodId`) REFERENCES `moods`(`id`)
-- );

-- CREATE TABLE `moods` (
--     `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `label` TEXT NOT NULL
-- );

-- select * from entries;

-- INSERT INTO entries
--     (concept, entry, date, moodId)
-- VALUES
--     (
--         'SQL',
--         'This is my first SQL entry.',
--         20201015,
--         1
--   );

-- INSERT INTO entries
--     (concept, entry, date, moodId)
-- VALUES
--     (
--         'Python',
--         "There's a Python in my boot!",
--         20200912,
--         2
--     );

-- INSERT INTO entries
--     (concept, entry, date, moodId)
-- VALUES
--     (
--         'SQL',
--         'Second SQL entry.',
--         20201015,
--         1
--     );

-- INSERT INTO moods
--     (label)
-- VALUES
--     (
--         'happy'
--     );

-- INSERT INTO moods
--     (label)
-- VALUES
--     (
--         'frustrated'
--     );

-- INSERT INTO moods
--     (label)
-- VALUES
--     (
--         'tired'
--     );

-- INSERT INTO moods
--     (label)
-- VALUES
--     (
--         'content'
--     );

-- INSERT INTO moods
--     (label)
-- VALUES
--     (
--         'angry'
--     );
