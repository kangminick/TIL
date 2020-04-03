# Android_Studio_Orientation

- 가로 세로 방향전환

```java
package org.techtown.orientation;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    String name;
    EditText editText;
    TextView textView2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        showToast("onCreate 호출됨");

        editText = findViewById(R.id.editText);
        textView2 = findViewById(R.id.textView2);

        Button button = findViewById(R.id.button);
        if (button != null) {

            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if (editText != null) {
                        name = editText.getText().toString();
                        showToast("사용자 입력값을 name 변수에 할당함");
                    }
                }
            });

            if (savedInstanceState != null) {
                if (textView2 != null) {
                    name = savedInstanceState.getString("name");
                    textView2.setText(name);

                    showToast("값을 복원했습니다 : " + name);
                }
            }
        }
    }
    @Override
    protected void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState);

        outState.putString("name", name);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();

        showToast("onDestroy 호출됨");
    }

    public void showToast(String data){
        Toast.makeText(this, data, Toast.LENGTH_SHORT).show();
    }
}

```

- 화면 초기환경 설정

AndroidManifest.xml 에 다음과 같은 코드 입력.

```java
<activity android:name=".MainActivity"
            android:configChanges="orientation|screenSize|keyboardHidden">
                
 android:screenOrientation="landscape" 
     //강제로 가로화면으로 시작됨.
 android:screenOrientation="portrait" 
     //강제로 세로화면으로 시작됨.       
```

```java
package org.techtown.orientation2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.res.Configuration;
import android.os.Bundle;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public void onConfigurationChanged(@NonNull Configuration newConfig) {
        super.onConfigurationChanged(newConfig);

        if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE){
            showToast("가로 방향임");
        } else if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT){
            showToast("세로 방향임");
        }
    }
    public void showToast(String data){
        Toast.makeText(this, data, Toast.LENGTH_SHORT).show();
    }
}

```

- Toast 메세지 출력

```java
package org.techtown.toast;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.Gravity;
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
                Toast toastView = Toast.makeText(getApplicationContext(), "토스트 메시지입니다.", Toast.LENGTH_LONG);
                toastView.setGravity(Gravity.Top|Gravity.LEFT, 200, 800);
                toastView.show();
            }
        });
    }
}
```