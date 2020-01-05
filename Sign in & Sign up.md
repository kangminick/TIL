## 회원가입

- application.properties

  DataSource

  ​	jdbc:h2:~/db명(embedded) → jdbc:h2:tcp://localhost/~/db명

```
# datasource
spring.datasource.url=jdbc:h2:tcp://localhost/~/board
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
# jpa
spring.jpa.hibernate.ddl-auto=update
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.show-sql=true
```

- model/User.java

```java
package com.example.board.model;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import lombok.Data;
@Entity
@Data
public class User {
@Id
@GeneratedValue(strategy = GenerationType.AUTO)
private long id;
private String email;
private String pwd;
private String name;
}
```

-  repository/UserRepository.java

```java
package com.example.board.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.example.board.model.User;
public interface UserRepository extends JpaRepository<User, Long> {
}
```

- controller/UserController.java

```java
package com.example.board.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import com.example.board.model.User;
import com.example.board.repository.UserRepository;
@Controller
public class UserController {
@Autowired
UserRepository userRepository;
@GetMapping("/signup")
public String signup() {
return "signup";
}
@PostMapping("/signup")
public String signupPost(@ModelAttribute User user) {
userRepository.save(user);
return "redirect:/";
}
}
```

-  http://localhost:8080/signup  

  회원가입 확인

## 로그인

> 필요 기술 / 라이브러리
>
> - HTML Design (bootstrap)
> - Database (H2)
> - JPA 
>   - Model (@Entity)
>   - ModelRepository (JpaRepository 상속)
> - Controller
> - Thymeleaf

- templates/signin.html

```html
...
<div class="jumbotron">
 <div class="container text-center">
 <form method="post" action="/signin">
 <div class="form-group">
 <label for="email">Email:</label>
 <input type="text" class="form-control" id="email" name="email">
 </div>
 <div class="form-group">
 <label for="pwd">Password:</label>
 <input type="password" class="form-control" id="pwd" name="pwd">
 </div>
 <button class="btn btn-primary btn-block" id="signin">Sign in</button>
 </form>
 </div>
 </div>
...
<script>
 $("#signin").click(function() {
 $("form").submit();
 return false;
 });
 </script>
```

-  repository/UserRepository.java

```java
package com.example.board.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.example.board.model.User;
public interface UserRepository extends JpaRepository<User, Long> {
public User findByEmailAndPwd(String email, String pwd);
}
```

- controller/UserController.java

```java
@Autowired
HttpSession session;
@GetMapping("/signin")
public String signin() {
return "signin";
}
@PostMapping("/signin")
public String signinPost(@ModelAttribute User user) {
User dbUser = userRepository.findByEmailAndPwd(user.getEmail(), user.getPwd());
if(dbUser != null) {
session.setAttribute("user_info", dbUser);
}
return "redirect:/";
}
```

-  http://localhost:8080/signin 로그인 확인