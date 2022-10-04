tic;
clear all
clf 
clc

xx=10;
yy=10;
cnt=0;

% Defining the obstacles... 
obstacles (1,:)=[0,3]; 
obstacles (2,:)=[1,1]; 
obstacles (3,:)=[2,1]; 
obstacles (4, :)=[2,3]; 
obstacles (5, :)=[3,1]; 
obstacles (6, :)=[3,2]; 
obstacles (7,:)=[3,3]; 
obstacles (8,:)=[3,5]; 
obstacles (9,:)=[3,7]; 
obstacles (10,:)=[4,3]; 
obstacles (11,:)=[4,5]; 
obstacles (12,:)=[5, 1]; 
obstacles (13,:)=[5,5]; 
obstacles (14,:)=[6,3]; 
obstacles (15,:)=[6,4]; 
obstacles (16,:)=[6,5]; 
obstacles (17,:)=[6,6]; 
obstacles (18,:)=[6,7]; 
obstacles (19,:)=[6,8]; 
obstacles (20,:)=[6,9]; 
obstacles (21,:)=[6,10]; 
obstacles (22,:)=[7, 2]; 
obstacles (23,:)=[7,3]; 
obstacles (24,:)=[8,5]; 
obstacles (25,:)=[9,3]; 
obstacles (26,:)=[9,5]; 
obstacles (27,:)=[10,3];
    

startingPosition=[5,7]; 
goal=[9,8];

obstacleColor=[1,0,0];  
nodeColor=[0,1,0]; 
expandColor=[0,0,0];  
goalColor=[0,0,1];  
pathColor=[0,1,1]; 

s = scatter (obstacles (:,1), obstacles (:,2), 150, ...
    obstacleColor, 'filled', 's', 'MarkerEdgeColor', 'b');

grid on;
%grid monor; 
%grid (gca, 'minor') 
set (gca, 'YMinorTick','on', 'XMinorTick','on') 
axis([0 10 0 10]); 
hold on;

scatter (goal(1,1), goal (1,2), 100, goalColor, 'filled');

pathCount=1; 

dfs_stack (pathCount, :)=[startingPosition, pathCount];


% This loop executes until the goal is found... 
while (~((dfs_stack (pathCount, 1) == goal (1,1)) &...
        (dfs_stack(pathCount, 2) == goal (1,2))))
    
    cnt=cnt+1
    scatter (dfs_stack(pathCount, 1), dfs_stack(pathCount, 2), ...
        100, nodeColor, 'filled');
% Exploring the neighbour (left right top bottom)... 
    for x=-1:1 
        for y=-1:1
            if (x*y==0)
                failsTest=0;
                tempNode=[dfs_stack(pathCount,1)+x, ...
                    dfs_stack(pathCount,2)+y, pathCount];

            if ( (tempNode (1,1)<0) | (tempNode(1,2)<0)) | ...
                    ( (tempNode(1,1)>xx) | (tempNode(1,2)>yy) ) 
                failsTest=failsTest+1; 
            end
% Test to see if node is already in dfs_stack set... 
            if (failsTest<1) 
                for i=1:size(dfs_stack,1) 
                    if (tempNode(1,1)==dfs_stack(i,1)) & ...
                            (tempNode(1,2)==dfs_stack(i,2)) 
                        failsTest=failsTest+1; 
                    end
                end
            end
            
            if (failsTest<1) 
                for i=1:size(obstacles,1) 
                    if (tempNode(1,1)==obstacles(i,1)) & ...
                            (tempNode(1,2)==obstacles(i,2))
                        failsTest=failsTest+1;
                    end
                end
            end
            
            if (failsTest<1) 
                if pathCount<size(dfs_stack, 1)
                    dfs_stack(size(dfs_stack, 1)+1,:)=[0,0,0]; 
                    prevNode=dfs_stack(pathCount+1,:);
                    
                    for i=(pathCount+2):(size(dfs_stack, 1))
                        nextNode = prevNode; 
                        prevNode = dfs_stack(i, :);
                        dfs_stack(i, :) = nextNode; 
                    end
                end
                dfs_stack (pathCount+1,:) = tempNode; 
                scatter (tempNode (1,1), tempNode (1,2), 120, ...
                    expandColor, 'filled'); 
            end
         end
      end
    end
    
    %Decrement tempCount as it is a position in the dfs_stack... 
    % Set relative to pathCount... 
    pathCount = pathCount+1;
    pause(.1); 
end

%Initialize a counter... 
i = 1;

while  ~(pathCount==1)
    path(i,:)=[dfs_stack(pathCount,1),dfs_stack(pathCount,2)]; 
    pathCount=dfs_stack(pathCount, 3);
    i=i+1; 
end

%Add the start position to the path 
   path(i, :)=startingPosition;
    
%Plot the path 
plot(path(:,1), path(:,2)); 
scatter (path(:,1), path(:,2), 60, pathColor,'filled',...
    'MarkerEdgeColor', 'b');

siz=(size(dfs_stack))
toc;