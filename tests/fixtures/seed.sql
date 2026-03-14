-- Inject dummy categories for tests
INSERT INTO categories (name, color)
VALUES
    ('health', '#FF5733'),
    ('learning', '#33FF57'),
    ('work', '#3357FF');

-- Inject dummy habits
INSERT INTO habits (category_id, name, description, frequency_type, frequency_target)
VALUES
    (1, 'Drink Water', 'Drink at least 8 glasses of water a day', 'daily', 8),
    (2, 'Read Book', 'Read 20 pages', 'daily', 1),
    (3, 'Review Code', 'Review PRs', 'weekly', 5);

-- Inject habit completions
INSERT INTO habit_completions (habit_id, note)
VALUES
    (1, 'Drank 2 glasses in the morning'),
    (1, 'Drank 4 glasses by noon');

-- Inject dummy standalone todos
INSERT INTO todos (category_id, habit_id, title, notes, priority, due_date)
VALUES
    (1, 1, 'Buy water bottle', 'Get a 1L bottle', 'high', date('now', '+2 days')),
    (2, NULL, 'Return library books', 'Need to return by Friday', 'medium', date('now', '+5 days'));
