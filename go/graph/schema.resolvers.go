package graph

// This file will be automatically regenerated based on the schema, any resolver implementations
// will be copied through when generating and any unknown code will be moved to the end.

import (
	"context"
	"fmt"
	"math/rand"

	"github.com/rexsimiloluwah/hello-graphql/go/graph/generated"
	"github.com/rexsimiloluwah/hello-graphql/go/graph/model"
)

func (r *mutationResolver) CreateTweet(ctx context.Context, input model.NewTweet) (*model.Tweet, error) {
	newTweet := model.Tweet{
		ID:      fmt.Sprintf("T%d", rand.Int()),
		Content: input.Content,
		User: &model.User{
			ID:       input.UserID,
			Username: "user-" + input.UserID,
		},
	}
	r.tweets = append(r.tweets, newTweet)
	return &newTweet, nil
}

func (r *queryResolver) Tweets(ctx context.Context) ([]*model.Tweet, error) {
	var tweets []*model.Tweet
	for _, tweet := range r.tweets {
		tweets = append(tweets, &tweet)
	}
	return tweets, nil
}

// Mutation returns generated.MutationResolver implementation.
func (r *Resolver) Mutation() generated.MutationResolver { return &mutationResolver{r} }

// Query returns generated.QueryResolver implementation.
func (r *Resolver) Query() generated.QueryResolver { return &queryResolver{r} }

type mutationResolver struct{ *Resolver }
type queryResolver struct{ *Resolver }
