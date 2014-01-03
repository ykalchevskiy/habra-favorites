# coding: utf-8

from scrapy.contrib.exporter import JsonItemExporter


class HtmlItemExporter(JsonItemExporter):

    FILE_START = """\
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Избранное</title>
    <script>
        var items = [
"""

    FILE_FINISH = """
        ];
        function makeTable(field) {
            var i, length = items.length,
                el, innerEl,
                main = document.getElementById('favorites');

            items.sort(function(l, r) {
                return r[field] - l[field];
            });
            main.innerHTML = '';
            for (i = 0; i < length; ++i) {
                innerEl = '<td>' + (i + 1) + '</td>' +
                        '<td><a href="' + items[i]['ref'] + '">' + items[i]['title'] + '</a></td>' +
                        '<td>' + items[i]['rating'] + '</td>' +
                        '<td>' + items[i]['count'] + '</td>' +
                        '<td>' + items[i]['views'] + '</td>' +
                        '<td>' + items[i]['comments'] + '</td>';
                el = document.createElement('tr');
                el.innerHTML = innerEl;

                main.appendChild(el);
            }
        }
    </script>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>Пост</th>
                <th onclick="makeTable('rating')">Рейтинг</th>
                <th onclick="makeTable('rating_all')">Голоса</th>
                <th onclick="makeTable('count')">Добавления</th>
                <th onclick="makeTable('views')">Просмотры</th>
                <th onclick="makeTable('comments')">Комментарии</th>
            </tr>
        </thead>
        <tbody id="favorites">
        </tbody>
    </table>
    <script>
        makeTable('rating');
    </script>
</body>
</html>
"""

    def start_exporting(self):
        self.file.write(self.FILE_START)

    def finish_exporting(self):
        self.file.write(self.FILE_FINISH)
