# 안드로이드 스튜디오

---

- 안드로이드 스튜디오 최신버전 다운로드 https://developer.android.com/studio?hl=ko
- 설치경로 (사용자이름) 한글이면 안된다.
- SDK Manager으로 임의로 개발할 버전을 선택할 수 있다.
- Package name = 고유한 App의 주소

---

1. Button

```java
// 1. xml에서 버튼을 생성, onclick에 onButton1Clicked 입력.

public void onButton1Clicked(view v) {
        Toast.makeText( this, "확인1 버튼이 눌렸어요.", Toast.LENGTH_LONG).show();
        //Toast : 버튼1을 누르면 하단에 텍스트가 출력됨
    }

// 2. xml에서 네이버 접속하기 버튼 생성, onclick에 onButton2Clicked 입력.

public void onButton2Clicked(view v) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://m.naver.com")); //intent는 변수명
        startActivity(intent); //Intent는 다른사람의 app을 띄울 수 있다.
    }

// 3. xml에서 전화하기 버튼 생성, onclick에 onButton3Clicked 입력.    

    public void onButton3Clicked(view v) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("tel:010-1000-1000"));
        startActivity(intent); 
    }
```

2. 디자인

- wrap_content  내용물의 크기에 맞게 
- match constraint 에서는 match parent가 동작하지 않는다. 
- match parent는 부모 레이아웃을 꽉 채워준다. 숫자지정도 가능 단위는 dp
- dp = 밀도 독립적 픽셀. 단말기마다 크기가 다른것을 보완.
- 테두리를 기준으로 바깥이 마진, 안쪽이 패딩. 뷰의 영역은 마진까지를 포함
- Layout_gravity 레이아웃 정렬, gravity 글짜 정렬

```java
//FrameLayout 버튼을 누르면 이미지 변경

package org.techtown.myframelayout;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {
    ImageView imageView; 
    ImageView imageView2;
    
    int imageIndex = 0;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        imageView = findViewById(R.id.imageView);
        imageView2 = findViewById(R.id.imageView2);
    }
    
    public void onButtonClicked(view v) {
        changeImage();
    }
    
    public void changeImage() {
        if (imageIndex == 0) {
            imageView.setVisibility(View.VISIBLE);
            imageView2.setVisibility(View.INVISIBLE);
            
            imageIndex = 1;
            
        }   else if (imageIndex == 1) {
            imageView.setVisibility(View.INVISIBLE);
            imageView2.setVisibility(View.VISIBLE);
        
            imageIndex = 0;
        }
    }
}
```

