# Android_Studio_Call

- Flag를 사용하면 스택에서 중복을 방지할 수 있다.

ex) FLAG_ACTIVITY_SINGLE_TOP

```
package org.techtown.callintent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("tel:010-1000-1000"));
//                전화가 아니라 url주소도 가능.
                startActivity(intent);

                /*Intent intent = new Intent();
                ComponentName name = new ComponentName("org.techtown.callintent",
                        "org.techtown.callintent.MenuActivity");
//                Menu액티비티를 띄워라
                intent.setComponent(name);
                startActivityForResult(intent, 101);*/
//                전화가 아닌 intent가 다른 용도로 쓰일 수 있다는 것을 보여주는 예시.
            }
        });
    }
}
```

