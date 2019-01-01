> 동명의 카지노에서 따온 이름을 가진, 무작위 추출된 난수를 이용하여 함수의 값을 계산하는 통계학의 방법. 
최적화, 수치적분, 확률분포로부터의 추출 등에 쓰인다.
<pre><code>
def pi_Taylor(n):
  pi = 0
  for i in xrange(n):
  pi=pi + 4.0/(2*i+1)*(-1)**i
  print i, pi

pi_Taylor(1000)
</code></pre>
> 아크탄젠트(arctan)는 다음과 같이 테일러 급수로 전개할 수 있다.
