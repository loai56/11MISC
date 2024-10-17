from flask import Flask, request, jsonify, send_from_directory
import csv
import os

app = Flask(__name__)

# 初始化CSV文件，检查文件是否存在，如果不存在则添加列名
def init_csv():
    if not os.path.exists('评分收集.csv'):
        with open('评分收集.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['姓名', '评价次数', '评分', '评价时间'])

# 保存评分信息到CSV文件
def save_rating(name, rating_count, score, timestamp):
    with open('评分收集.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, rating_count, score, timestamp])

# 路由返回主页（11点痛苦量表.html）
@app.route('/')
def index():
    # 修改路径为你实际的HTML文件路径
    return send_from_directory(
        'E:/1.博士/⭐⭐⭐⭐⭐⭐⭐⭐⭐舒适性研究⭐⭐⭐⭐⭐⭐⭐⭐/1.实验/评分网页',
        '11点痛苦量表.html'
    )

# 处理评分提交请求
@app.route('/submit-rating', methods=['POST'])
def submit_rating():
    data = request.get_json()
    name = data.get('name')
    rating_count = data.get('rating_count')
    score = data.get('score')
    timestamp = data.get('timestamp')

    if name and score and timestamp and rating_count:
        save_rating(name, rating_count, score, timestamp)
        return jsonify({'message': '评分已提交！'}), 200
    else:
        return jsonify({'message': '数据无效！请确保填写姓名、评分和时间。'}), 400

if __name__ == '__main__':
    init_csv()  # 确保CSV文件初始化
    app.run(host='0.0.0.0', port=5000, debug=True)



