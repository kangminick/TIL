# Android_Studio_ActionBar_OptionMenu

- 타이틀, 버튼, 입력상자를 통해 검색가능
- res에 menu라는 디렉토리를 만들고 menu_main.xml 생성

```java
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <item android:id="+@id/menu_refresh"
        android:title="새로고침"
        android:icon="@drawable/menu_refresh"
        app:showAsAction="always" />

    <item android:id="+@id/menu_search"
        android:title="검색"
        android:icon="@drawable/menu_search"
        app:showAsAction="always" />

    <item android:id="+@id/menu_settings"
        android:title="설정"
        android:icon="@drawable/menu_settings"
        app:showAsAction="always" />
    // 상단에 아이콘 3개 추가.
    
</menu>
```

- MainActivity.java

```java
package org.techtown.optionmenu;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    ActionBar actionBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        actionBar = getSupportActionBar();  
        
        actionBar.setLogo(R.drawable.home);
        actionBar.setDisplayOptions(ActionBar.DISPLAY_SHOW_HOME|ActionBar.DISPLAY_USE_LOGO);
        // 왼쪽 상단의 글자가 home 이미지로 대체된다.
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        
        return true;
    }
    // 메뉴를 처음에 설정해주는 함수

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        int curId = item.getItemId();
        
        switch (curId) {
            case R.id.menu_refresh:
                showToast("새로고침 메뉴 선택");
            case R.id.menu_search:
                showToast("검색 메뉴 선택");
            case R.id.menu_settings:
                showToast("설정 메뉴 선택");
                break;
            default:
                break;
        }
        return super.onOptionsItemSelected(item);
    }
    // 메뉴 아이템이 선택(클릭) 되었을 때 실행되는 함수
    
    public  void showToast(String data) {
        Toast.makeText(this, data, Toast.LENGTH_LONG).show();
    } 
}

```

