# 안드로이드 스튜디오 

### Part02 chapter 03 01

- strings.xml 의 속성 값을 참조할 수 있다. ex) @string/myname
- 이미지를 바꾸고 싶을 때에는 srcCompat을 이용



```java
버튼을 꾸며줄때. xml 파일을 만들어 설정해 줄 수 있다.
    
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_pressed="true"
        android:drawable="@drawable/ic_launcher_background"/>
<!--   버튼을 눌렀을때->
    <item android:drawable="@drawable/ic_launcher_foreground"/>
<!--    기본상태-->
</selector>
```

```java
임의의 도형을 만들 수 있다.
    
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <size android:width="200dp" android:height="120dp" />
    <stroke android:width="1dp" android:color="#0000ff"/>
<!--    stroke는 테두리선-->
    <solid android:color="#aaddff" />
    <padding android:bottom="1dp"/>
</shape>
```

```java
색상 효과를 줄 수 있다.

<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient
        android:startColor="#7288DB"
        android:centerColor="#3250B4"
        android:endColor="#254095"
        android:angle="90"
        android:centerY="0.5"/>
    <corners android:radius="5dp"/>
</shape>
```

```java
테두리 디자인을 할 수 있다.

<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item>
        <shape android:shape="rectangle">
            <stroke android:width="1dp" android:color="#be55da"/>
            <solid android:color="#00000000"/>
            <size android:width="200dp" android:height="100dp"/>
        </shape>
    </item>
    <item android:top="1dp" android:bottom="1dp"
        android:right="1dp" android:left="1dp">
        <shape android:shape="rectangle">
            <stroke android:width="1dp" android:color="#ff55da"/>
            <solid  android:color="#00000000"/>
        </shape>
    </item>
</layer-list>
```



