import tensorflow as tf
# 아래 os 부분은 CPU 성능이 안좋은 경우 뜨는 경고 메시지를 무시하기 위해 작성
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data = [[2, 2, 79], [3, 3, 85], [4, 6, 97], [5, 3, 92]]
x1_data = [x_row[0] for x_row in data]
x2_data = [x_row[1] for x_row in data]
y_data = [y_row[2] for y_row in data]

# 기울기 a, y절편 b 값을 임의로 설정
"""
변수를 정할 때 Variable() 함수 사용, random_uniform()은 임의의 수 설정
random.uniform([1], 0, 10, ..)은 0에서 10 사이에서 임의의 수 1개 설정하라는 뜻, dtype = float64, seed = 0 실행 시 같은 값
"""
a1 = tf.Variable(tf.random.uniform([1], 0, 10, tf.float64, 0))
a2 = tf.Variable(tf.random.uniform([1], 0, 10, tf.float64, 0))
b = tf.Variable(tf.random.uniform([1], 0, 100, tf.float64, 0))

y = a1 * x1_data + a2 * x2_data+ b

# Tensorflow RMSE function
rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))

# 학습률
learning_rate = 0.1

# RMSE = 평균 제곱근 오차를 최소로 하는 값 찾기 = 가장 오차가 적은 직선 찾기
gradient_descent = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

# Learning used Tensorflow
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())  # 초기화
    for step in range(2001):  # 2001번 실행 0 ~ 2000
        sess.run(gradient_descent)
        if step % 100 == 0:
            print("Epoch : %.f, RMSE : %.5f, 기울기 a1 : %.5f, 기울기 a2 : %.5f, y절편 b : %.5f"
                  % (step, sess.run(rmse), sess.run(a1), sess.run(a2), sess.run(b)))

# Epoch : 입력 값에 대하여 몇 번 반복하여 실험했는지 보여줌