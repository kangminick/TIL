# Android_Studio_LifeCycle

- 수명주기에 따른 상태변화. 수명주기는 앱을 사용하다 다른 활동(전화)를 하고 왔을때 앱의 상태를 결정짓는다.
- 종료했다가 다시 시작했을때 이전의 데이터를 불러 올 수 있다.

```java
package org.techtown.lifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    
    EditText editText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        editText = findViewById(R.id.editText);

        Log.d("Main","onCreate 호출됨");
    }

    @Override
    protected void onStart() {
        super.onStart();

        Log.d("Main","onStart 호출됨");
    }

    @Override
    protected void onStop() {
        super.onStop();

        Log.d("Main","onStop 호출됨");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();

        Log.d("Main","onDestroy 호출됨");
    }

    @Override
    protected void onPause() {
        super.onPause();

        saveState();
//        저장
        Log.d("Main","onPause 호출됨");
    }

    @Override
    protected void onResume() {
        super.onResume();

        loadState();
//        복원
        Log.d("Main","onResume 호출됨");
    }
    
    public void saveState() {
        SharedPreferences pref = getSharedPreferences("pref", Activity.MODE_PRIVATE);
        SharedPreferences.Editor editor = pref.edit();
        editor.putString("name", editText.getText().toString());
        editor.commit();
    }
//    세이브
    
    public void loadState(){
        SharedPreferences pref = getSharedPreferences("pref", Activity.MODE_PRIVATE);
        if (pref != null){
            String name = pref.getString("name", "");
            editText.setText(name);
        }
    }
//    불러오기
}
```

