# Android_Studio_Intent

1. 화면간 데이터 전달 ex(사용자 정보, 로그인)
2. Intent에 데이터를 넣어서 화면전환
3. class 변수에 데이터를 넣고 참조하는 방식

---

- 두개의 Activity가 합쳐서 하나의 화면을 구성해본다.
- MainActivity

```java
package org.techtown.intent;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), MenuActivity.class);
//                menuActivity를 지정하는 Intent 객채를 생성하고 지정한 것.
//        getApplicationContext는 사용되는 공통 context를 참조할 수 있게 해준다.

                startActivityForResult(intent, 101);
//                액티비티를 실행했을 때, 요청 코드를 통해 응답을 구분할 수 있다.
            }
        });
    }
    //아래가 데이터 받기
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 101) {
            if (data != null) {
                String name = data.getStringExtra("name");
                if (name != null) {
                    Toast.makeText(this, "응답으로 받은 데이터 : " + name, Toast.LENGTH_LONG).show();
                }
            }
        }
    }
}
```

- MenuActivity

```java
package org.techtown.intent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.putExtra("name", "mike");
                //intent를 통해서 다른 액티비티로 데이터를 전송할 수 있다.
                setResult(200, intent);
                // ResultCode를 RESULT_OK로 보내서 정상응답로 구분 할 수 있다.

                finish(); //화면이 없어진다. 대신 꺼지지않고 밑으로 깔려있는다.
            } //여기까지가 데이터 전송
        });
    }
}
```

