class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        courses =  [0 for i in range(numCourses)]

        hash_map ={}

        count =0


        for i, j in prerequisites:
            courses[i]+=1

            if j in hash_map:
                hash_map[j].append(i)
            else:
                hash_map[j]=[i]

        queue = deque()

        for i in range(len(courses)):

            if courses[i]==0:
                queue.append(i)
                count+=1


        if(count == numCourses):
            return True


        while(queue):

            current_course = queue.popleft()

            if current_course in hash_map:

                dependent_courses = hash_map[current_course]

                for course in dependent_courses:

                    courses[course]-=1

                    if courses[course]==0:
                        queue.append(course)
                        count+=1

                        if(count == numCourses):
                            return True


        return False
